package com.MedAmbulance.Activity.ui.home;

import android.Manifest;
import android.animation.ValueAnimator;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.DialogInterface;
import android.content.IntentSender;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.location.Location;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.os.Handler;
import android.os.StrictMode;
import android.os.SystemClock;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.AccelerateDecelerateInterpolator;
import android.view.animation.Interpolator;
import android.view.animation.LinearInterpolator;
import android.widget.CompoundButton;
import android.widget.LinearLayout;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.app.ActivityCompat;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProviders;

import com.MedAmbulance.Activity.DriversMapsActivity;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Regular;
import com.MedAmbulance.util.AppUtil;
import com.crowdfire.cfalertdialog.CFAlertDialog;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GooglePlayServicesUtil;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.PendingResult;
import com.google.android.gms.common.api.ResultCallback;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationCallback;
import com.google.android.gms.location.LocationListener;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationResult;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.location.LocationSettingsRequest;
import com.google.android.gms.location.LocationSettingsResult;
import com.google.android.gms.location.LocationSettingsStatusCodes;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.CameraPosition;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MapStyleOptions;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.material.switchmaterial.SwitchMaterial;

import org.eclipse.paho.client.mqttv3.DisconnectedBufferOptions;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttAsyncClient;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class HomeFragment extends Fragment implements OnMapReadyCallback, GoogleApiClient.ConnectionCallbacks,GoogleApiClient.OnConnectionFailedListener
        , LocationListener {

    private static final String TAG = "DRIVERS";

    private static final int REQUEST_CHECK_SETTINGS =  93;
    private   static  final  int PLAYSERVICE_RES__REQUEST_CODE=301;

    private HomeViewModel homeViewModel;
    MySharedPrefrence sharedPreferences;
    String userId,reqestTopic;
    String locationTopic="";
    LinearLayout linearLayout;
    LocationListener locationListener;
    SupportMapFragment mapFragment;
    SwitchMaterial switchMaterial;
    Marker mCurrent,mPrev,mSrc,mDest;
    ArrayList<String> topiclist=new ArrayList<String>();
    MqttAsyncClient mqttAndroidClient;
    private FusedLocationProviderClient FPclient;
    private LocationRequest locationRequest;
    final String serverUri = "tcp://134.209.153.34:1883";
    private  Location location,prevlocation;
    private  GoogleApiClient googleApiClient;
    private boolean isAccepted;
    private JSONObject currentRequest;
    final String  base_url="http://134.209.153.34:5077/";
    private GoogleMap mMap;
    private boolean isBook;
    private boolean isHide;
    boolean isMarkerRotating;
    private List<LatLng> polyList;
    int index=0;
    int next=0;
    LatLng end,start;
    float v;
    Double  lng,lat;
    private  static  final  int PERMISSION_REQUEST_CODE=300;
    String clientId = "dClient";

    private static  final int UPDATE_INTERVAL=100;
    private static  final int FASTEST_INTERVAL=3000;
    private static  final int DISPLACEMENT=10;

    private Runnable drawPathRunnable=new Runnable() {
        @Override
        public void run() {
            if(polyList!=null){
                if(index<polyList.size()-1){
                    index++;
                    next=index+1;
                }
            }
            if(index<polyList.size()-1){
                start= polyList.get(index);
                end= polyList.get(next);

            }

            final ValueAnimator valueAnimator=ValueAnimator.ofFloat(0,1);
            valueAnimator.setDuration(3000);
            valueAnimator.setDuration(3000);
            valueAnimator.setInterpolator(new LinearInterpolator());
            valueAnimator.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
                @Override
                public void onAnimationUpdate(ValueAnimator animation) {
                    v= valueAnimator.getAnimatedFraction();
                    lng=v*end.longitude+(1-v)*start.longitude;
                    lat =v*end.latitude+(1-v)*start.latitude;
                    LatLng newPos=new LatLng(lat,lng);
                    mCurrent.setPosition(newPos);
                    mCurrent.setAnchor(0.5f,0.5f);
                    mCurrent.setRotation(getBearing(start,newPos));
                    mMap.moveCamera(CameraUpdateFactory.newCameraPosition(new CameraPosition.Builder().target(newPos).zoom(15.5f)
                            .build()));
                }
            });
        }
    };

    private float getBearing(LatLng start, LatLng newPos) {

        double lat= Math.abs(start.latitude-end.latitude);
        double lng=Math.abs(start.longitude-end.longitude);
        if(start.latitude<end.latitude && start.longitude<end.longitude){
            return  (float)(Math.toDegrees(Math.atan(lng/lat)));
        }

        else  if(start.latitude>=end.latitude && start.longitude<end.longitude){
            return  (float)((90-Math.toDegrees(Math.atan(lng/lat)))+90);
        } else  if(start.latitude>=end.latitude && start.longitude>=end.longitude){
            return  (float)(Math.toDegrees(Math.atan(lng/lat))+180);
        } else  if(start.latitude<end.latitude && start.longitude>=end.longitude){
            return  (float)((90-Math.toDegrees(Math.atan(lng/lat)))+270);
        }
        return  -1;
    }

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {

        homeViewModel =
                ViewModelProviders.of(this).get(HomeViewModel.class);
        View root = inflater.inflate(R.layout.fragment_home, container, false);
        sharedPreferences =  MySharedPrefrence.instanceOf(getContext());
        userId=sharedPreferences.getUserId();
        reqestTopic=  userId+"/"+"booking";
        locationTopic=  userId;

        StrictMode.ThreadPolicy threadPolicy = new StrictMode.ThreadPolicy.Builder().build();
        StrictMode.setThreadPolicy(threadPolicy);

        locationListener=this;
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        mapFragment = (SupportMapFragment) getChildFragmentManager().findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);


        switchMaterial=root.findViewById(R.id.location_switch);
        switchMaterial=root.findViewById(R.id.location_switch);
        linearLayout=root.findViewById(R.id.accept_liner);
        switchMaterial.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isOnline) {
                if(isOnline){
                    startLocationUpdates();
                    //   displayLocation();
                    if(mCurrent!=null){
                        mCurrent.setVisible(true);
                    }
                    if(!topiclist.contains(reqestTopic)){
                        topiclist.add(reqestTopic);
                    }
                    coonectMqtt(reqestTopic);
                    linearLayout.setVisibility(View.VISIBLE);
                    AppUtil.bottomSnakBar(getContext(),mapFragment.getView(),"You are online");
                }else {
                    try {
                        mqttAndroidClient.disconnect();
                    } catch (MqttException e) {
                        e.printStackTrace();
                    }
                    stopLocationUpdates();
                    if(mCurrent!=null){
                        mCurrent.setVisible(false);
                    }
                    linearLayout.setVisibility(View.INVISIBLE);
                    AppUtil.bottomSnakBar(getContext(),mapFragment.getView(),"You are offline");
                }
            }

        });
        setUpLocation();

        setUpMqtt();
        return root;
    }

    private void setUpMqtt() {



        //mqtt
        clientId = clientId + System.currentTimeMillis();
        try {
            mqttAndroidClient = new MqttAsyncClient( serverUri, clientId,null);

            mqttAndroidClient.setCallback(new MqttCallbackExtended() {
                @Override
                public void connectComplete(boolean reconnect, String serverURI) {

                    if (reconnect) {
                        addToHistory("Reconnected to : " + serverURI);
//                    // Because Clean Session is true, we need to re-subscribe
                        for(String topics:topiclist) {
                            subscribeToTopic(topics);
                        }

                    } else {
                        addToHistory("Connected to: " + serverURI);
                    }
                }

                @Override
                public void connectionLost(Throwable cause) {
                    addToHistory("The Connection was lost.");
                }

                @Override
                public void messageArrived(String topic, MqttMessage message) throws Exception {
                    addToHistory("Incoming message: " + new String(message.getPayload()));


                    if(topic.equalsIgnoreCase(reqestTopic)){

                        final JSONObject jsonObject=new JSONObject( new String(message.getPayload()));
                        getActivity().runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                requestPopup(jsonObject);
                            }
                        });
                    }

                }

                @Override
                public void deliveryComplete(IMqttDeliveryToken token) {

                }
            });

        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    public void requestPopup(final JSONObject jsonObject){
        currentRequest=jsonObject;
        Log.d("popub","new request");
        @SuppressLint("ResourceType") final CFAlertDialog.Builder builder = new CFAlertDialog.Builder(getContext())
                .setDialogStyle(CFAlertDialog.CFAlertStyle.BOTTOM_SHEET).setCancelable(false)
//                .setTitle("You've hit the limit")
               //    .setDialogBackgroundResource(R.layout.accept_ride_dialog)
//                .setMessage("Looks like you've hit your usage limit. Upgrade to our paid plan to continue without any limits.")
                .addButton("Accept", -1, -1, CFAlertDialog.CFAlertActionStyle.POSITIVE, CFAlertDialog.CFAlertActionAlignment.JUSTIFIED, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        //Toast.makeText(DriversMapsActivity.this, "Upgrade tapped", Toast.LENGTH_SHORT).show();

                        String api_url = base_url+"acceptRide";

                        Log.d("accept",jsonObject.toString());
                        JSONObject response_data = call_api(api_url, jsonObject.toString());
                        try {
                            if(response_data.getString("status").equalsIgnoreCase("true")){
                                isAccepted=true;
                                dialog.dismiss();
                                setUiOnAccept(jsonObject);//arrivedPopup(jsonObject);
                            }else {
                                isAccepted=false;
                                AppUtil.topSnakBar(getContext(),mapFragment.getView(),response_data.getString("message"));
                            }
                            //  Log.d("accept",response_data.toString());

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                })
                .addButton("Decline", -1, -1, CFAlertDialog.CFAlertActionStyle.DEFAULT, CFAlertDialog.CFAlertActionAlignment.JUSTIFIED, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        // Toast.makeText(DriversMapsActivity.this, "Upgrade tapped", Toast.LENGTH_SHORT).show();
                        dialog.dismiss();
                    }
                });
        LayoutInflater inflater = getLayoutInflater();



        View myLayout = inflater.inflate(R.layout.request_popup_view,null, false);
        Atami_Regular from= myLayout.findViewById(R.id.from);
        Atami_Regular  to= myLayout.findViewById(R.id.to);
        final Atami_Regular  time= myLayout.findViewById(R.id.time);

        from.setText(AppUtil.getDatafromJSonObject(jsonObject,"pickupLocationAddress"));
        to.setText(AppUtil.getDatafromJSonObject(jsonObject,"dropLocationAddress"));

        LinearLayout tl= (LinearLayout)myLayout. findViewById(R.id.tl);
        tl.setVisibility(View.VISIBLE);

        new CountDownTimer(30000, 1000) {

            public void onTick(long millisUntilFinished) {
                time.setText("" + millisUntilFinished / 1000);
            }

            public void onFinish() {

                time.setText("done!");
            }
        }.start();
        builder.setAutoDismissAfter(30000);
        builder.setHeaderView(myLayout);

        builder.setFooterView(null);

// Show the alert
        builder.show();
    }

    private void setUpLocation() {
        if (ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_COARSE_LOCATION)!= PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED
        ){

            ActivityCompat.requestPermissions(getActivity(),new String[]{

                    Manifest.permission.ACCESS_COARSE_LOCATION,
                    Manifest.permission.ACCESS_FINE_LOCATION

            },PERMISSION_REQUEST_CODE);
        }else {

            if(checkPlayServices()){

                buildGoogleClient();
                createLocationRequest();
                if(switchMaterial.isChecked()){
                    displayLocation();
                }
            }
        }
    }

    private void createLocationRequest() {
        locationRequest=new LocationRequest();
        locationRequest.setInterval(UPDATE_INTERVAL);
        locationRequest.setFastestInterval(FASTEST_INTERVAL);
        locationRequest.setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY);
        locationRequest.setSmallestDisplacement(DISPLACEMENT);
    }

    private void buildGoogleClient() {
        googleApiClient=new GoogleApiClient.Builder(getContext()).addConnectionCallbacks(this
        ).addOnConnectionFailedListener(this).addApi(LocationServices.API).build();

        googleApiClient.connect();
    }

    private boolean checkPlayServices() {

        int resultcode= GooglePlayServicesUtil.isGooglePlayServicesAvailable(getActivity());

        if(resultcode!= ConnectionResult.SUCCESS){
            if(GooglePlayServicesUtil.isUserRecoverableError(resultcode)){

                GooglePlayServicesUtil.getErrorDialog(resultcode,getActivity(),PLAYSERVICE_RES__REQUEST_CODE).show();
            }else{

                AppUtil.showToastMsg("This Device is Not Supported",getContext());
                getActivity().finish();
            }

            return false;

        }
        return  true;
    }

    private void setUiOnAccept(JSONObject jsonObject) {
        Log.d("set up ui on accept","");
        try{

            Double srcLat=Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject,"startLocationLat"));
            Double srcLng=Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject,"startLocationLong"));
            Double  destLat=Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject,"dropLocationLat"));
            Double  destLng=Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject,"dropLocationLong"));


            LatLng destination_location=new LatLng(destLat,destLng);
            LatLng src_location=new LatLng(srcLat,srcLng);
            if (mSrc != null) {
                mSrc.remove();
            }
            MarkerOptions markerOptions = new MarkerOptions();
            markerOptions.position(src_location);
            markerOptions.title("Source");

            BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.marker_new);
            Bitmap b = bitmapDrawable.getBitmap();
            Bitmap smallCar = Bitmap.createScaledBitmap(b, 150, 81, false);

            markerOptions.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
//                markerOptions.rotation(location.getBearing());
            mSrc = mMap.addMarker(markerOptions);
            if (mDest != null) {
                mDest.remove();
            }



            MarkerOptions markerOptions1 = new MarkerOptions();
            markerOptions1.position(destination_location);
            markerOptions1.title("Destination");
            BitmapDrawable bitmapDrawable1 = (BitmapDrawable) getResources().getDrawable(R.drawable.destination_marker);
            Bitmap b1 = bitmapDrawable1.getBitmap();
            Bitmap dest = Bitmap.createScaledBitmap(b1, 150, 81, false);

            markerOptions1.icon(BitmapDescriptorFactory.fromBitmap(dest));
            ///markerOptions.rotation(latLng.getBearing());
            mDest = mMap.addMarker(markerOptions1);
            if (mSrc!=null && mDest!=null && mCurrent!=null) {
                String url = getDirectionsUrl(mCurrent.getPosition(), mSrc.getPosition());
                String url1 = getDirectionsUrl(mSrc.getPosition(), mDest.getPosition());
//        DownloadTask downloadTask = new DownloadTask(false);
//
//           // Start downloading json data from Google Directions API
//           downloadTask.execute(url1);
                DownloadTask downloadTask1 = new DownloadTask(true);

                // Start downloading json data from Google Directions API
                downloadTask1.execute(url);
                //Animation




            } else {

            }

        }catch (Exception e){  Log.d("set up ui on accept",""+e);}

        Log.d("set up ui on accept",""+"end");

    }

    @Override
    public void onResume() {
        super.onResume();
        showGpsSettingsAlert(getContext());
    }

    private void showGpsSettingsAlert(Context context) {
        GoogleApiClient googleApiClient = new GoogleApiClient.Builder(context)
                .addApi(LocationServices.API).build();
        googleApiClient.connect();

        LocationRequest locationRequest = LocationRequest.create();
        locationRequest.setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY);
        locationRequest.setInterval(10000);
        locationRequest.setFastestInterval(10000 / 2);

        LocationSettingsRequest.Builder builder = new LocationSettingsRequest.Builder().addLocationRequest(locationRequest);
        builder.setAlwaysShow(true);

        PendingResult<LocationSettingsResult> result = LocationServices.SettingsApi.checkLocationSettings(googleApiClient, builder.build());
        result.setResultCallback(new ResultCallback<LocationSettingsResult>() {
            @Override
            public void onResult(LocationSettingsResult result) {
                final Status status = result.getStatus();
                switch (status.getStatusCode()) {
                    case LocationSettingsStatusCodes.SUCCESS:
                        Log.i(TAG, "All location settings are satisfied.");
                        break;
                    case LocationSettingsStatusCodes.RESOLUTION_REQUIRED:
                        Log.i(TAG, "Location settings are not satisfied. Show the user a dialog to upgrade location settings ");

                        try {
                            // Show the dialog by calling startResolutionForResult(), and check the result
                            // in onActivityResult().
                            status.startResolutionForResult(getActivity(), REQUEST_CHECK_SETTINGS);
                        } catch (IntentSender.SendIntentException e) {
                            Log.i(TAG, "PendingIntent unable to execute request.");
                        }
                        break;
                    case LocationSettingsStatusCodes.SETTINGS_CHANGE_UNAVAILABLE:
                        Log.i(TAG, "Location settings are inadequate, and cannot be fixed here. Dialog not created.");
                        break;
                }
            }
        });
    }

    public void coonectMqtt(final String topic){
        addToHistory("topic: " + topic );

        MqttConnectOptions mqttConnectOptions = new MqttConnectOptions();
        mqttConnectOptions.setAutomaticReconnect(true);
        mqttConnectOptions.setCleanSession(false);


        try {
            //addToHistory("Connecting to " + serverUri);
            mqttAndroidClient.connect(mqttConnectOptions, null, new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    DisconnectedBufferOptions disconnectedBufferOptions = new DisconnectedBufferOptions();
                    disconnectedBufferOptions.setBufferEnabled(true);
                    disconnectedBufferOptions.setBufferSize(100);
                    disconnectedBufferOptions.setPersistBuffer(false);
                    disconnectedBufferOptions.setDeleteOldestMessages(false);
                    mqttAndroidClient.setBufferOpts(disconnectedBufferOptions);
                    //    publishMessage("topic","connected");
                    subscribeToTopic(topic);
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    addToHistory("Failed to connect to: " + serverUri);
                    addToHistory("Failed to connect to: " + exception.getMessage());
                }
            });


        } catch (MqttException ex){
            ex.printStackTrace();
        }
    }


    private void addToHistory(String mainText){
        Log.d("mqtt",mainText);
//        System.out.println("LOG: " + mainText);
//        mAdapter.add(mainText);
//        Snackbar.make(findViewById(android.R.id.content), mainText, Snackbar.LENGTH_LONG)
//                .setAction("Action", null).show();
    }

    public void subscribeToTopic( String topic){
        try {
            mqttAndroidClient.subscribe(topic, 0, null, new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    addToHistory("Subscribed!");
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    addToHistory("Failed to subscribe");
                }
            });

            // THIS DOES NOT WORK!
//            mqttAndroidClient.subscribe(subscriptionTopic, 0, new IMqttMessageListener() {
//                @Override
//                public void messageArrived(String topic, MqttMessage message) throws Exception {
//                    // message Arrived!
//                    addToHistory("Message: " + topic + " : " + new String(message.getPayload()));
//                }
//            });

        } catch (MqttException ex){
            addToHistory("Exception whilst subscribing");
            ex.printStackTrace();
        }
    }

    private void startLocationUpdates() {
        Log.d("location","request for update");
        if (ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_COARSE_LOCATION)!= PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED
        ){

            return;
        }
        FPclient = LocationServices.getFusedLocationProviderClient(getContext());
        FPclient.requestLocationUpdates(locationRequest,
                new LocationCallback() {
                    @Override
                    public void onLocationResult(LocationResult locationResult) {
                        Log.d("aaaaaasd",locationResult.toString());
//Get a reference to the database, so your app can perform read and write operations//

                        prevlocation=location;
                        location = locationResult.getLastLocation();

                        if (location != null) {


                            AppUtil.showToastMsg("new "+ location.getLatitude(),getContext());
//Save the location data to the database//
                            displayLocation();

                        }
                    }
                }, null);
        if(googleApiClient.isConnected()){
            Log.d("location","request for update1");
            //  LocationServices.FusedLocationApi. requestLocationUpdates(googleApiClient,locationRequest, (com.google.android.gms.location.LocationListener) locationListener);
        }}

    private void stopLocationUpdates() {
        Log.d("location","stop for update");
        if (ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_COARSE_LOCATION)!= PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED
        ){

            return;
        }
        if(FPclient!=null){

            FPclient.removeLocationUpdates(new LocationCallback());
            FPclient=null;
        }
        // LocationServices.FusedLocationApi.removeLocationUpdates(googleApiClient, (com.google.android.gms.location.LocationListener) locationListener);
    }

    @Override
    public void onConnected(@Nullable Bundle bundle) {
        if(switchMaterial.isChecked()){
            startLocationUpdates();
            displayLocation();}
    }

    @Override
    public void onConnectionSuspended(int i) {
        googleApiClient.connect();
    }

    @Override
    public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {

    }

    @Override
    public void onLocationChanged(Location location) {
        // AppUtil.showToastMsg("new "+ location.getLatitude(),getApplicationContext());
//        Log.d("location","location");
//          Log.d("location",location.toString());
//        displayLocation();
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        try{
            boolean isSuccess=googleMap.setMapStyle(MapStyleOptions.loadRawResourceStyle(getContext(),R.raw.uber_style_map));
        }catch (Exception e){
            e.printStackTrace();
        }
        mMap = googleMap;
    }

    private void displayLocation() {

        Log.d("location","display location");

        if (ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_COARSE_LOCATION)!= PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED
        ){

            return;
        }
        // prevlocation=location;
        //location= LocationServices.FusedLocationApi.getLastLocation(googleApiClient);
        if(location!=null){

            if(switchMaterial.isChecked()){

                final    double lat=location.getLatitude();
                final    double lng=location.getLongitude();

                Log.d("mqtt location:",lat+"-"+lng);

                if(isAccepted && currentRequest!=null){
                    Log.d("location","need publish");
                    try {
                        currentRequest.put("ambulanceLat",lat+"");
                        currentRequest.put("ambulanceLng",lng+"");
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    publishMessage(locationTopic,currentRequest.toString());
                }else {
                    String api_url = base_url + "updateDriverLatLong";


                    JSONObject jsonObject = new JSONObject();
                    try {
                        jsonObject.put("lat", lat + "");

                        jsonObject.put("lng", lng + "");
                        jsonObject.put("driverId", sharedPreferences.getUserId());
                        JSONObject response_data = call_api(api_url, jsonObject.toString());
                        if (response_data != null)
                            Log.d("send_loc", response_data.toString());
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                if(prevlocation==null || mCurrent==null ){
                    if(mCurrent!=null){
                        mCurrent.remove();
                    }
                    MarkerOptions markerOptions= new MarkerOptions();

                    BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.amb);
                    Bitmap b = bitmapDrawable.getBitmap();
                    Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);

                    markerOptions.icon( BitmapDescriptorFactory.fromBitmap(smallCar));
                    markerOptions.position(new LatLng(lat,lng));
                    markerOptions.title("you");

                    mCurrent=mMap.addMarker(markerOptions);
                    mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(lat,lng),15.0f));

                    Log.d("move"," no move car");

                }else{
                    Log.d("move","move car");
                    movecar();
                }
                if (mSrc!=null && mDest!=null && mCurrent!=null) {
                    String url = getDirectionsUrl(mCurrent.getPosition(), mSrc.getPosition());
                    String url1 = getDirectionsUrl(mSrc.getPosition(), mDest.getPosition());
//        DownloadTask downloadTask = new DownloadTask(false);
//
//           // Start downloading json data from Google Directions API
//           downloadTask.execute(url1);
                    DownloadTask downloadTask1 = new DownloadTask(true);

                    // Start downloading json data from Google Directions API
                    downloadTask1.execute(url);
                    //Animation




                } else {

                }
                if(prevlocation!=null){

                    mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(lat,lng),15.0f));
                    rotateMarker(mCurrent, (float) bearingBetweenLocations(prevlocation,location),mMap);
                    Log.d("bb",(float) bearingBetweenLocations(prevlocation,location)+"");
                }


                if(isBook){
//                    mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(lat,lng),15.0f));
//
//                    rotateMarker(mCurrent,-360,mMap);}else{

                    //  rotateMarker(mCurrent, (float) bearingBetweenLocations(prevlocation,location));

                }


            }

        }
//       if(FPclient!=null){
//        FPclient.requestLocationUpdates(locationRequest,
//                new LocationCallback() {
//            @Override
//            public void onLocationResult(LocationResult locationResult) {
//                   Log.d("aaaaaasd",locationResult.toString());
////Get a reference to the database, so your app can perform read and write operations//
//                  location = locationResult.getLastLocation();
//                if(location!=null){
//
//                    if(switchMaterial.isChecked()){
//
//                        final    double lat=location.getLatitude();
//                        final    double lng=location.getLongitude();
//
//                        Log.d("mqtt location:",lat+"-"+lng);
//
//                        if(isAccepted && currentRequest!=null){
//
//                            publishMessage(locationTopic,currentRequest.toString());
//                        }else {
//                            String api_url = base_url + "updateDriverLatLong";
//
//
//                            JSONObject jsonObject = new JSONObject();
//                            try {
//                                jsonObject.put("lat", lat + "");
//
//                                jsonObject.put("lng", lng + "");
//                                jsonObject.put("driverId", sharedPreferences.getUserId());
//                                JSONObject response_data = call_api(api_url, jsonObject.toString());
//                                if (response_data != null)
//                                    Log.d("send_loc", response_data.toString());
//                            } catch (JSONException e) {
//                                e.printStackTrace();
//                            }
//                          }
//
//                        if(mCurrent!=null){
//                            mCurrent.remove();
//                        }
//                        MarkerOptions markerOptions= new MarkerOptions();
//
//                        BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.amb);
//                        Bitmap b = bitmapDrawable.getBitmap();
//                        Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);
//
//                        markerOptions.icon( BitmapDescriptorFactory.fromBitmap(smallCar));
//                        markerOptions.position(new LatLng(lat,lng));
//                        markerOptions.title("you");
//
//                        mCurrent=mMap.addMarker(markerOptions);
//                        if (mSrc!=null && mDest!=null && mCurrent!=null) {
//                            String url = getDirectionsUrl(mCurrent.getPosition(), mSrc.getPosition());
//                            String url1 = getDirectionsUrl(mSrc.getPosition(), mDest.getPosition());
////        DownloadTask downloadTask = new DownloadTask(false);
////
////           // Start downloading json data from Google Directions API
////           downloadTask.execute(url1);
//                            DownloadTask downloadTask1 = new DownloadTask(true);
//
//                            // Start downloading json data from Google Directions API
//                            downloadTask1.execute(url);
//                            //Animation
//
//
//
//
//                        } else {
//
//                        }
//
//                        if(!isBook){
//                            mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(lat,lng),15.0f));
//
//                            rotateMarker(mCurrent,-360,mMap);}
//
//
//                    }
//
//                }
//
//            }
//        }, null);}else {

        //}
    }

    public void publishMessage(String locationTopic,String msg){
        Log.d("location","publish"+msg);
        Log.d("msgg",locationTopic+"----"+msg);
        try {
            MqttMessage message = new MqttMessage();
            message.setPayload(msg.getBytes());
            mqttAndroidClient.publish(locationTopic, message);
            addToHistory("Message Published");
            if(!mqttAndroidClient.isConnected()){
                addToHistory(mqttAndroidClient.getBufferedMessageCount() + " messages in buffer.");
            }
        } catch (MqttException e) {
            System.err.println("Error Publishing: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public JSONObject call_api(String api_url, String request_data) {
        try {

            Log.d("API_res",api_url);
            URL url = new URL(api_url);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setDoInput(true);
            conn.setDoOutput(true);
            OutputStream os = conn.getOutputStream();
            BufferedWriter writer = new BufferedWriter(
                    new OutputStreamWriter(os, "UTF-8"));

            writer.write(request_data);
            writer.flush();
            writer.close();
            os.close();

            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line = "";
            String response = "";
            while ((line = bufferedReader.readLine()) != null) {
                response += line;
            }
            Log.d("API_res",response);
            Log.d("API response", response);

            JSONObject response_data = new JSONObject(response);
            return response_data;

        } catch (Exception e) {
//            Toast.makeText(getApplicationContext(),e.toString(),Toast.LENGTH_LONG).show();
            Log.d("API_res",e.toString());
        }

        return null;
    }

    public void movecar(){
        final Location startPosition =prevlocation ;
        final Location finalPosition = location;
        final Handler handler = new Handler();
        final long start = SystemClock.uptimeMillis();
        final Interpolator interpolator = new AccelerateDecelerateInterpolator();
        final float durationInMs = 3000;
        final boolean hideMarker = false;

        handler.post(new Runnable() {
            long elapsed;
            float t;
            float v;

            @Override
            public void run() {
                // Calculate progress using interpolator
                elapsed = SystemClock.uptimeMillis() - start;
                t = elapsed / durationInMs;
                v = interpolator.getInterpolation(t);

                LatLng currentPosition = new LatLng(
                        startPosition.getLatitude()*(1-t)+finalPosition.getLatitude()*t,
                        startPosition.getLongitude()*(1-t)+finalPosition.getLongitude()*t);

                mCurrent.setPosition(currentPosition);
                Log.d("move.....................","move car");
                // Repeat till progress is complete.
                if (t < 1) {
                    // Post again 16ms later.
                    handler.postDelayed(this, 16);
                } else {
                    if (hideMarker) {
                        mCurrent.setVisible(false);
                    } else {
                        mCurrent.setVisible(true);
                        isHide=true;
                    }
                }
            }
        });
    }

    private String getDirectionsUrl(LatLng origin, LatLng dest) {

        // Origin of route
        String str_origin = "origin=" + origin.latitude + "," + origin.longitude;

        // Destination of route
        String str_dest = "destination=" + dest.latitude + "," + dest.longitude;

        // Sensor enabled
        String sensor = "sensor=false";
        String key = "key=AIzaSyDRVBkjjZkrZf-_blL06aGAeQ2uSCuJRn8";
        //mode
        String  mode = "mode=driving";
        //transit
        String   transit = "transit_routing_preference=less_driving";
        // Building the parameters to the web service
        String parameters = str_origin + "&" + str_dest + "&" + sensor+"&"+key+"&"+mode +"&"+ transit;

        // Output format
        String output = "json";

        // Building the url to the web service
        // Building the url to the web service
        String url = "https://maps.googleapis.com/maps/api/directions/" + output + "?" + parameters;

        Log.d("result",url);
//my code
        // String url =   "http://www.yournavigation.org/api/1.0/gosmore.php?flat="+ origin.latitude+"&flon="+origin.longitude+"&tlat="+ dest.latitude +"&tlon="+ dest.longitude +"&format=geojson";


        //end my code

        return url;
    }
    private class DownloadTask extends AsyncTask<String, Void, String> {
        boolean isBooked = false;

        public DownloadTask(boolean isBooked) {
            this.isBooked = isBooked;
            isBook = isBooked;
        }

        // Downloading data in non-ui thread
        @Override
        protected String doInBackground(String... url) {

            // For storing data from web service
            String data = "";

            try {
                // Fetching the data from web service
                data = downloadUrl(url[0]);

                Log.d("Background Task", data);
            } catch (Exception e) {
                Log.d("Background Task", e.toString());
            }
            return data;
        }
    }

    private String downloadUrl(String strUrl) throws IOException {
        String data = "";
        InputStream iStream = null;
        HttpURLConnection urlConnection = null;
        try {
            URL url = new URL(strUrl);

            // Creating an http connection to communicate with url
            urlConnection = (HttpURLConnection) url.openConnection();

            // Connecting to url
            urlConnection.connect();

            // Reading data from url
            iStream = urlConnection.getInputStream();

            BufferedReader br = new BufferedReader(new InputStreamReader(iStream));

            StringBuffer sb = new StringBuffer();

            String line = "";
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }

            data = sb.toString();

            br.close();

        } catch (Exception e) {
//            Log.d("Exception while downloading url", e.toString());
        } finally {
            iStream.close();
            urlConnection.disconnect();
        }
        return data;
    }

    private void rotateMarker(final Marker marker, final float toRotation) {
        if(!isMarkerRotating) {
            final Handler handler = new Handler();
            final long start = SystemClock.uptimeMillis();
            final float startRotation = marker.getRotation();
            final long duration = 1000;

            final Interpolator interpolator = new LinearInterpolator();

            handler.post(new Runnable() {
                @Override
                public void run() {
                    isMarkerRotating = true;

                    long elapsed = SystemClock.uptimeMillis() - start;
                    float t = interpolator.getInterpolation((float) elapsed / duration);

                    float rot = t * toRotation + (1 - t) * startRotation;

                    marker.setRotation(-rot > 180 ? rot / 2 : rot);
                    if (t < 1.0) {
                        // Post again 16ms later.
                        handler.postDelayed(this, 16);
                    } else {
                        isMarkerRotating = false;
                    }
                }
            });
        }
    }

    private double bearingBetweenLocations(Location latLng1, Location latLng2) {

        double PI = 3.14159;
        double lat1 = latLng1.getLatitude() * PI / 180;
        double long1 = latLng1.getLongitude() * PI / 180;
        double lat2 = latLng2.getLatitude() * PI / 180;
        double long2 = latLng2.getLongitude() * PI / 180;

        double dLon = (long2 - long1);

        double y = Math.sin(dLon) * Math.cos(lat2);
        double x = Math.cos(lat1) * Math.sin(lat2) - Math.sin(lat1)
                * Math.cos(lat2) * Math.cos(dLon);

        double brng = Math.atan2(y, x);
        brng = Math.toDegrees(brng);
        brng = (brng + 360) % 360;
        return brng;
    }

    private void rotateMarker(final Marker mCurrent, final float i, GoogleMap mMap) {
        final Handler handler=new Handler();
        final long start= SystemClock.uptimeMillis();
        final float startRotation=  mCurrent.getRotation();
        final long duration=1500;
        final Interpolator interpolator=new LinearInterpolator();
        handler.post(new Runnable() {
            @Override
            public void run() {

                long elapsed=SystemClock.uptimeMillis()-start;
                float t= interpolator.getInterpolation((float)elapsed/duration);
                float rot=t*i+(1-t)*startRotation;
                mCurrent.setRotation(-rot>180?rot/2:rot);

                if(t<1.0){
                    handler.postDelayed(this,16);                }
            }
        }) ;
    }
}
