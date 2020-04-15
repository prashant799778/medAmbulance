package com.MedAmbulance.Fragments;

import android.Manifest;
import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.IntentSender;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.graphics.drawable.BitmapDrawable;
import android.location.Address;
import android.location.Geocoder;
import android.content.SharedPreferences;
import android.location.Location;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
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
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Activity.Countinue_As_Acrtivity;
import com.MedAmbulance.Activity.DestinationActivity;
import com.MedAmbulance.Activity.DriversMapsActivity;
import com.MedAmbulance.Activity.End_Ride_Activity;
import com.MedAmbulance.Activity.MapsActivity;
import com.MedAmbulance.Activity.ui.home.HomeFragment;
import com.MedAmbulance.Adapters.Horizontal_adapter;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Model.Ambulance;
import com.MedAmbulance.Model.EndRideModel;
import com.MedAmbulance.Model.QuestionModel;
import com.MedAmbulance.Model.RateCardModel;
import com.MedAmbulance.Model.SupportModel;
import com.MedAmbulance.Model.YourRidesModel;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;
import com.MedAmbulance.util.AppUtil;
import com.MedAmbulance.util.DirectionsJSONParser;
import com.MedAmbulance.util.PlaceJSONParserTemp;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.error.VolleyError;
import com.android.volley.request.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.crowdfire.cfalertdialog.CFAlertDialog;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
import com.google.android.gms.common.GooglePlayServicesRepairableException;
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
import com.google.android.gms.location.places.Place;
import com.google.android.gms.location.places.ui.PlaceAutocomplete;
import com.google.android.gms.location.places.ui.PlacePicker;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.CameraPosition;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.LatLngBounds;
import com.google.android.gms.maps.model.MapStyleOptions;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.maps.model.Polyline;
import com.google.android.gms.maps.model.PolylineOptions;
import com.google.android.material.card.MaterialCardView;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.eclipse.paho.client.mqttv3.DisconnectedBufferOptions;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttAsyncClient;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.json.JSONArray;
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
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Timer;

import static android.app.Activity.RESULT_CANCELED;
import static android.app.Activity.RESULT_OK;
import static android.content.Context.MODE_PRIVATE;
import static com.MedAmbulance.Fragments.UserBookYourRideFragment.MY_PERMISSIONS_REQUEST_LOCATION;

public class BookYourRideFrgment extends Fragment implements OnMapReadyCallback,
        GoogleApiClient.ConnectionCallbacks,
        GoogleApiClient.OnConnectionFailedListener,
        LocationListener, MyResult {

    private static final int REQUEST_CHECK_SETTINGS = 93;
    int flag = 0;
    boolean isSourceSet = false, tripStarted = false;
    ;
    EditText source_location, destination_location;
    String TAG = "LocationSelect";
    int AUTOCOMPLETE_SOURCE = 1, AUTOCOMPLETE_DESTINATITON = 2;
    GoogleMap mMap;

    //textView
    Atami_Regular text_als, text_bls, text_dbt, text_pvt;

    MyResult myResult;
    ArrayList<QuestionModel> questionModelArrayList;
    GoogleApiClient mGoogleApiClient;
    Location mLastLocation;
    Marker mCurrLocationMarker, source_location_marker, destination_location_marker;
    Marker nearby_cab;
    LinearLayout location_field_layout, selection_layout, bottomlayout, AIR;
    ArrayList<Marker> markers = new ArrayList<Marker>();
    ;
    LocationRequest mLocationRequest;
    ArrayList<LatLng> markerPoints;
    Button btnBookNow;
    MaterialCardView for_ambulance, for_responder, for_noraml, for_govt, ALS, BLS, DBT, PVT;
//    ImageView cab;


    String ambulanceModeId = "", ambulanceTypeId = "";
    RelativeLayout driver_info;
    String  Questionid="";
    LatLng user_latlong = null;
    MarkerOptions markerOptions1;
    LinearLayout ll_call, ll_share, ll_cancel, btnBookNow_layout;
    String driver_name, cab_no, cab_id, otp, fare, driver_phone, ride_id, driverLat, drivetLng, driverId, pickup_Lat, pickup_long;
    TextView cab_no_a, cab_no_b, ride_otp, ride_driver_name, ride_fare;
    //    Atami_Regular text_als,text_bls,text_dbt,text_pvt;
    String PREFS_NAME = "auth_info";
    ProgressDialog progressDialog;
    Timer timer;
    Polyline polyline, driverPolyline;
    Handler handler;
//     MyResult myResult;

    JSONArray currentNearbyCabs = new JSONArray();
    //mqtt
    MqttAsyncClient mqttAndroidClient;
    final String base_url = "http://134.209.153.34:5077/";
    final String serverUri = "tcp://134.209.153.34:1883";
    ArrayList<String> topiclist = new ArrayList<String>();
    String clientId = "dClient";
    final String subscriptionTopic = "outTopic";
    final String publishTopic = "outTopic";
    String userId, bookTopic, DriverLocationTopic, driverArriveTopic, startRideTopic, endRideTopic, paymentTopic;

    final String publishMessage = "Hello World!";

    /////


    MySharedPrefrence sharedPreferences;
    private LatLng ambulance_latlng;
    String userTypeId = "";
    private LatLng dest_lating;
    private LatLng prevlocationAmb;
    private Marker ambMarker;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        this.myResult = this;
        View rootView = inflater.inflate(R.layout.frag_book_your_ride, container, false);
        Api_Calling.getMethodCall(getContext(), URLS.selectambulanceMaster, getActivity().getWindow().getDecorView(), myResult, "show text", showText());

        sharedPreferences = MySharedPrefrence.instanceOf(getActivity());
        userId = sharedPreferences.getUserId();

        //topic intialize

        questionModelArrayList = new ArrayList<>();
        bookTopic = userId + "/" + "booking";
        DriverLocationTopic = userId + "/" + "ambulanceLiveLocation";
        driverArriveTopic = userId + "/" + "arrive";
        startRideTopic = userId + "/" + "startRide";
        endRideTopic = userId + "/" + "endRide";
        paymentTopic = userId + "/" + "payment";
        topiclist.add(driverArriveTopic);
        topiclist.add(bookTopic);
        topiclist.add(DriverLocationTopic);
        topiclist.add(startRideTopic);
        topiclist.add(endRideTopic);
        topiclist.add(paymentTopic);


        ////end

        handler = new Handler();

        driver_info = (RelativeLayout) rootView.findViewById(R.id.driver_details);

        driver_info.setVisibility(View.GONE);

        progressDialog = new ProgressDialog(getActivity());
        progressDialog.setMessage("Booking...");
        progressDialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);
        progressDialog.setIndeterminate(true);
        progressDialog.setCancelable(true);

        ll_call = (LinearLayout) rootView.findViewById(R.id.ll_call);
        ll_share = (LinearLayout) rootView.findViewById(R.id.ll_share);
        ll_cancel = (LinearLayout) rootView.findViewById(R.id.ll_cancel);

        cab_no_a = (TextView) rootView.findViewById(R.id.cab_no_a);
        cab_no_b = (TextView) rootView.findViewById(R.id.cab_no_b);
        ride_driver_name = (TextView) rootView.findViewById(R.id.driver_name);
        ride_otp = (TextView) rootView.findViewById(R.id.ride_otp);
        ride_fare = (TextView) rootView.findViewById(R.id.ride_fare);
        btnBookNow_layout = (LinearLayout) rootView.findViewById(R.id.btnBookNow_layout);
        btnBookNow = (Button) rootView.findViewById(R.id.btnBookNow);
        btnBookNow.setVisibility(View.GONE);
        btnBookNow_layout.setVisibility(View.GONE);
        location_field_layout = rootView.findViewById(R.id.enterlayout);
        location_field_layout.setVisibility(View.GONE);
        selection_layout = rootView.findViewById(R.id.t1);
        for_ambulance = rootView.findViewById(R.id.hospital);
        for_responder = rootView.findViewById(R.id.responsder);
        for_noraml = rootView.findViewById(R.id.normal);
        for_govt = rootView.findViewById(R.id.Govt);
        bottomlayout = rootView.findViewById(R.id.bottomlayout);
        ALS = rootView.findViewById(R.id.ALS);
        BLS = rootView.findViewById(R.id.BLS);
        DBT = rootView.findViewById(R.id.DBT);
        PVT = rootView.findViewById(R.id.PVT);
        AIR = rootView.findViewById(R.id.AIR);
//        user_latlong=new LatLng(,);
//        for_noraml.setEnabled(false);
//        for_responder.setEnabled(false);
//        for_ambulance.setEnabled(false);
//        for_govt.setEnabled(false);


        for_noraml.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (user_latlong != null)
                    showBottomLayout("2");
                userTypeId = "1";
            }
        });
        for_govt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (user_latlong != null)
                    userTypeId = "1";
                showBottomLayout("1");

            }
        });
        for_ambulance.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (user_latlong != null)
                    userTypeId = "1";
                showBottomLayout("3");
            }
        });
        for_responder.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (user_latlong != null) {
                    setNearbyCabsOnMap(user_latlong, "2", "", "");
                    selection_layout.setVisibility(View.GONE);
                    location_field_layout.setVisibility(View.VISIBLE);
                    userTypeId = "2";
                }

            }
        });
//        location_field_layout.setVisibility(View.VISIBLE);
//        selection_layout.setVisibility(View.GONE);
        Utility.log("Arrievd MQTTT", ":" + driverArriveTopic);

//        cab = (ImageView) rootView.findViewById(R.id.cab);
//        cab.setVisibility(View.GONE);

        timer = new Timer();

        markerPoints = new ArrayList<LatLng>();

        StrictMode.ThreadPolicy threadPolicy = new StrictMode.ThreadPolicy.Builder().build();
        StrictMode.setThreadPolicy(threadPolicy);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            checkLocationPermission();
        }

        source_location = (EditText) rootView.findViewById(R.id.source_location);
        destination_location = (EditText) rootView.findViewById(R.id.destination_location);

        setupUi(rootView);
        btnBookNow.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                progressDialog.show();
                if (currentNearbyCabs != null && currentNearbyCabs.length() > 0) {
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            // show dialog here
                            //progressDialog.show();
                        }
                    });
                    try {

                        String api_url = base_url + "bookRide";
                        Log.d("book_ride", api_url);
                        double src_lat = source_location_marker.getPosition().latitude;
                        double src_lng = source_location_marker.getPosition().longitude;
                        String src_add = source_location.getText().toString();

                        double dest_lat = destination_location_marker.getPosition().latitude;
                        double dest_lng = destination_location_marker.getPosition().longitude;
                        String dest_add = destination_location.getText().toString();
                        String user_id = sharedPreferences.getUserId();
                        JSONObject jsonObject = new JSONObject();
                        jsonObject.put("userId", user_id).put("driverId", currentNearbyCabs)
                                .put("startLocationLat", src_lat).put("startLocationLong", src_lng)
                                .put("pickupLocationAddress", src_add).put("dropLocationLat", dest_lat)
                                .put("dropLocationLong", dest_lng).put("dropLocationAddress", dest_add);

                        Log.d("book", jsonObject.toString());
//                    String user_id = sharedPreferences.getString("id", null);
//
//                    String book_now_request = "user_id=" + URLEncoder.encode(user_id, "UTF-8") + "&src_lat=" + URLEncoder.encode(String.valueOf(src_lat), "UTF-8") + "&src_lng=" + URLEncoder.encode(String.valueOf(src_lng), "UTF-8") + "&dest_lat=" + URLEncoder.encode(String.valueOf(dest_lat), "UTF-8") + "&dest_lng=" + URLEncoder.encode(String.valueOf(dest_lng), "UTF-8");

                        JSONObject response_data = call_api(api_url, jsonObject.toString());

                        //JSONObject response_data=new JSONObject();

//                    response_data.put("status","true");
//                    JSONObject response_data1=new JSONObject();
//
//                    response_data1.put("bookingId","1");
//                    response_data1.put("cab_no","DL 123456");
//                    response_data1.put("ambulanceId","1");
//                    response_data1.put("driver_name","Driver3"); response_data1.put("driverMobile","7905469882");
//                    response_data1.put("otp","98799");
//                    response_data1.put("fare","245");
//                    response_data.put("data",response_data1);
//
//
//
//
//               progressDialog.dismiss();


                        if (response_data.getString("status").equals("True")) {
                            if (!topiclist.contains(bookTopic)) {
                                topiclist.add(bookTopic);
                                Utility.log("TopicPublished", "" + bookTopic);
                            }
                            coonectMqtt(bookTopic);

                        } else {
//                            progressDialog.dismiss();
                            Toast.makeText(getActivity(), "No cabs nearby", Toast.LENGTH_LONG).show();
                        }

                    } catch (Exception e) {
                        Toast.makeText(getActivity(), e.getMessage(), Toast.LENGTH_LONG).show();
                    }
                } else {
                    noNearAmlumancePopup();
                }
            }
        });


//        Toast.makeText(getApplicationContext(), this.toString(), Toast.LENGTH_LONG).show();
        final Activity activity = getActivity();

        source_location.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if (b) {
                    try {
//                        Intent intent =
//                                new PlaceAutocomplete.IntentBuilder(PlaceAutocomplete.MODE_OVERLAY).build(activity);
//                        startActivityForResult(intent, AUTOCOMPLETE_SOURCE);
                        PlacePicker.IntentBuilder builder = new PlacePicker.IntentBuilder();
                        startActivityForResult(builder.build(activity), AUTOCOMPLETE_SOURCE);
                    } catch (GooglePlayServicesRepairableException e) {
                        // TODO: Handle the error.
//                        Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
                    } catch (GooglePlayServicesNotAvailableException e) {
                        // TODO: Handle the error.
//                        Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();

                    }
                }
            }
        });


        source_location.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
//                    Intent intent =
//                            new PlaceAutocomplete.IntentBuilder(PlaceAutocomplete.MODE_OVERLAY).build(activity);
//                    startActivityForResult(intent, AUTOCOMPLETE_SOURCE);
                    PlacePicker.IntentBuilder builder = new PlacePicker.IntentBuilder();
                    startActivityForResult(builder.build(activity), AUTOCOMPLETE_SOURCE);
                } catch (GooglePlayServicesRepairableException e) {
                    // TODO: Handle the error.
//                    Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
                } catch (GooglePlayServicesNotAvailableException e) {
                    // TODO: Handle the error.
//                    Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();

                }
            }
        });


        destination_location.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
//                Toast.makeText(getApplicationContext(), "Destination", Toast.LENGTH_SHORT).show();
                if (b) {
//                    try {
////                        Intent intent =
////                                new PlaceAutocomplete.IntentBuilder(PlaceAutocomplete.MODE_OVERLAY).build(activity);
////                        startActivityForResult(intent, AUTOCOMPLETE_DESTINATITON);
//                        PlacePicker.IntentBuilder builder = new PlacePicker.IntentBuilder();
//                        startActivityForResult(builder.build(activity), AUTOCOMPLETE_DESTINATITON);
//                    } catch (GooglePlayServicesRepairableException e) {
//                        // TODO: Handle the error.
////                        Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
//                    } catch (GooglePlayServicesNotAvailableException e) {
//                        // TODO: Handle the error.
////                        Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
//
//                    }


                    Intent intent = new Intent(getActivity(), DestinationActivity.class);

                    startActivityForResult(intent, AUTOCOMPLETE_DESTINATITON);
                }
            }
        });


        destination_location.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent intent = new Intent(getActivity(), DestinationActivity.class);

                startActivityForResult(intent, AUTOCOMPLETE_DESTINATITON);
//                try {
////                    Intent intent =
////                            new PlaceAutocomplete.IntentBuilder(PlaceAutocomplete.MODE_OVERLAY).build(activity);
////                    startActivityForResult(intent, AUTOCOMPLETE_DESTINATITON);
//                    PlacePicker.IntentBuilder builder = new PlacePicker.IntentBuilder();
//                    startActivityForResult(builder.build(activity), AUTOCOMPLETE_DESTINATITON);
//                } catch (GooglePlayServicesRepairableException e) {
//                    // TODO: Handle the error.
////                    Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
//                } catch (GooglePlayServicesNotAvailableException e) {
//                    // TODO: Handle the error.
////                    Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
//
//                }
            }
        });


//


        SupportMapFragment mapFragment = (SupportMapFragment) getChildFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);


        mqttSetup();
        return rootView;
    }

    private Object showText() {

        JSONObject jsonObject = new JSONObject();

        return jsonObject;
    }


    public Runnable runnable = new Runnable() {
        @Override
        public void run() {
            MarkerOptions markerOptions1;
            try {

                String api_url = "get_cab_location";

                String get_cab_location_request = "cab_id=" + URLEncoder.encode(cab_id, "UTF-8") + "&ride_id=" + URLEncoder.encode(ride_id, "UTF-8");

                JSONObject response_data = call_api(api_url, get_cab_location_request);

//                Toast.makeText(getApplicationContext(), response_data.toString(), Toast.LENGTH_LONG).show();

                if (response_data.getString("status").equals("1")) {
                    if (nearby_cab != null) {
                        nearby_cab.remove();
                    }

                    markerOptions1 = new MarkerOptions();
                    JSONObject get_cab_position_response_data = response_data.getJSONObject("data");


                    LatLng nearby_cab_position = new LatLng(Double.parseDouble(get_cab_position_response_data.getString("cab_lat")), Double.parseDouble(get_cab_position_response_data.getString("cab_lng")));
                    markerOptions1.position(nearby_cab_position);

                    BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.car);
                    Bitmap b = bitmapDrawable.getBitmap();
                    Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);
                    markerOptions1.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
                    markerOptions1.rotation(Float.parseFloat(get_cab_position_response_data.getString("cab_bearing")));
                    nearby_cab = mMap.addMarker(markerOptions1);
                    handler.postDelayed(this, 10000);
                } else if (response_data.getString("status").equals("2")) {
                    ll_cancel.setClickable(false);
                    handler.removeCallbacksAndMessages(runnable);
                    if (nearby_cab != null) {
                        nearby_cab.remove();
                    }
                    tripStarted = true;
//                    cab.setVisibility(View.VISIBLE);
                } else if (response_data.getString("status").equals("3")) {
                    ll_cancel.setClickable(false);
                    handler.removeCallbacksAndMessages(runnable);
                } else {
                    handler.postDelayed(this, 10000);
                }

            } catch (Exception e) {
                handler.postDelayed(this, 10000);
            }
        }
    };

    public JSONObject call_api(String api_url, String request_data) {
        try {
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

            Log.d("API response", response);

            JSONObject response_data = new JSONObject(response);
            return response_data;

        } catch (Exception e) {
//            Toast.makeText(getApplicationContext(),e.toString(),Toast.LENGTH_LONG).show();
        }

        return null;
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);


        Utility.log("Result---",""+data);
        if (requestCode == AUTOCOMPLETE_SOURCE) {
            if (resultCode == RESULT_OK) {
                Place place = PlacePicker.getPlace(getActivity(), data);
                Log.i(TAG, "Place: " + place.getName());
                source_location.setText(place.getName());

                if (source_location_marker != null) {
                    source_location_marker.remove();
                }

                LatLng latLng = place.getLatLng();
                MarkerOptions markerOptions = new MarkerOptions();
                markerOptions.position(latLng);
                markerOptions.title("Source");

                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.marker_new);
                Bitmap b = bitmapDrawable.getBitmap();
                Bitmap smallCar = Bitmap.createScaledBitmap(b, 150, 81, false);

                markerOptions.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
//                markerOptions.rotation(location.getBearing());
                source_location_marker = mMap.addMarker(markerOptions);

                mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(source_location_marker.getPosition(), 15.0f));
                setNearbyCabsOnMap(latLng, userTypeId, ambulanceTypeId, ambulanceModeId);
                user_latlong = latLng;

//                for_noraml.setEnabled(true);
//                for_responder.setEnabled(true);
//                for_ambulance.setEnabled(true);
//                for_govt.setEnabled(true);
//
//
//                for_noraml.setEnabled(false);
//                for_responder.setEnabled(false);
//                for_ambulance.setEnabled(false);
//                for_govt.setEnabled(false);


                Utility.log("Lcoation", "OnActivityResult  ----LAtitude---" + user_latlong.latitude + "---Longnitude----" + user_latlong.longitude);


            } else if (resultCode == PlaceAutocomplete.RESULT_ERROR) {
                Status status = PlaceAutocomplete.getStatus(getActivity(), data);
                // TODO: Handle the error.
                Log.i(TAG, status.getStatusMessage());

            } else if (resultCode == RESULT_CANCELED) {
                // The user canceled the operation.
            }
        } else if (requestCode == AUTOCOMPLETE_DESTINATITON) {
            if (resultCode == RESULT_OK && data != null) {
//                Place place = PlaceAutocomplete.getPlace(this, data);
                //  Place place = PlacePicker.getPlace(this, data);
                // Log.i(TAG, "Place: " + place.getName());


                String[] datas = data.getStringArrayExtra("result");
                destination_location.setText(datas[0]);

                if (destination_location_marker != null) {
                    destination_location_marker.remove();
                }


                LatLng latLng = new LatLng(Double.parseDouble(datas[1]), Double.parseDouble(datas[2]));
                MarkerOptions markerOptions = new MarkerOptions();
                markerOptions.position(latLng);
                markerOptions.title("Destination");
                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.destination_marker);
                Bitmap b = bitmapDrawable.getBitmap();
                Bitmap dest = Bitmap.createScaledBitmap(b, 150, 81, false);

                markerOptions.icon(BitmapDescriptorFactory.fromBitmap(dest));
                ///markerOptions.rotation(latLng.getBearing());
                destination_location_marker = mMap.addMarker(markerOptions);


                if (!source_location.getText().toString().equals("") && !destination_location.getText().toString().equals("")) {
                    String url = getDirectionsUrl(source_location_marker.getPosition(), destination_location_marker.getPosition());
//                    DownloadTask downloadTask = new DownloadTask(false);
//
//                    // Start downloading json data from Google Directions API
//                    downloadTask.execute(url);

                    btnBookNow.setVisibility(View.VISIBLE);
                    btnBookNow_layout.setVisibility(View.VISIBLE);
                } else {
                    btnBookNow.setVisibility(View.GONE);
                    btnBookNow_layout.setVisibility(View.GONE);
                }

            } else if (resultCode == PlaceAutocomplete.RESULT_ERROR) {
                Status status = PlaceAutocomplete.getStatus(getActivity(), data);
                // TODO: Handle the error.
                Log.i(TAG, status.getStatusMessage());

            } else if (resultCode == RESULT_CANCELED) {
                // The user canceled the operation.
            }
        }
    }

    //NearBy Ambulance
    public void setNearbyCabsOnMap(LatLng latLng, String driverTypeid, String Typeid, String modelType) {
        try {
            String api_url = base_url + "getNearAmbulance";
//
            double user_lat = latLng.latitude;
            double user_lng = latLng.longitude;


            //    String pickup_location_cabs_request = "user_lat=" + URLEncoder.encode(String.valueOf(user_lat), "UTF-8") + "&user_lng=" + URLEncoder.encode(String.valueOf(user_lng), "UTF-8");
            JSONObject pickup_location_cabs_request = new JSONObject();
            pickup_location_cabs_request.put("startLocationLat", user_lat);
            pickup_location_cabs_request.put("startLocationLong", user_lng);
            pickup_location_cabs_request.put("driverTypeId", "" + driverTypeid);
            pickup_location_cabs_request.put("ambulanceTypeId", "" + Typeid);
            pickup_location_cabs_request.put("ambulanceModeId", "" + modelType);
            Utility.log("MapTesting", "OnsetNearbyCabsOnMap" + pickup_location_cabs_request);
            JSONObject response_data = call_api(api_url, pickup_location_cabs_request.toString());
            currentNearbyCabs = new JSONArray();
            Log.d("near_cab", response_data.toString());
            ArrayList<Ambulance> ambulances = new ArrayList<>();

            if (response_data.getString("status").equalsIgnoreCase("true")) {
                JSONArray jsonArray1 = response_data.getJSONArray("ambulanceTypeId");
                JSONArray jsonArray = response_data.getJSONArray("result");
                Log.d("near_cab", "true" + jsonArray.length());

                for (Marker marker : markers) {
                    marker.remove();
                }
                markers.clear();
                for (int i = 0; i < jsonArray.length(); i++) {
                    Log.d("near_cab", "true");
                    Ambulance ambulance = new Ambulance();
                    JSONObject jo = jsonArray.getJSONObject(i);
                    ambulance.setAmbId(AppUtil.getDatafromJSonObject(jo, "ambulanceId"));
                    currentNearbyCabs.put(AppUtil.getDatafromJSonObject(jo, "driverId"));

                    ambulance.setAmbNo(AppUtil.getDatafromJSonObject(jo, "ambulanceNo"));
                    ambulance.setDistance(AppUtil.getDatafromJSonObject(jo, "distance"));
                    ambulance.setDriverName(AppUtil.getDatafromJSonObject(jo, "name"));
                    ambulance.setLat(AppUtil.getDatafromJSonObject(jo, "lat"));
                    ambulance.setLng(AppUtil.getDatafromJSonObject(jo, "lng"));
                    ambulance.setMobileNo(AppUtil.getDatafromJSonObject(jo, "mobileNo"));
                    ambulances.add(ambulance);

                    ///map work
                    markerOptions1 = new MarkerOptions();


                    LatLng nearby_cab_position = new LatLng(Double.parseDouble(ambulance.getLat()), Double.parseDouble(ambulance.getLng()));
                    markerOptions1.position(nearby_cab_position);
                    BitmapDrawable bitmapDrawable = new BitmapDrawable();
                    if (driverTypeid.equalsIgnoreCase("1")) {
                        bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.amb);
                    } else {
                        bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.responder);
                    }
                    Bitmap b = bitmapDrawable.getBitmap();
                    Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);

                    markerOptions1.icon(BitmapDescriptorFactory.fromBitmap(smallCar));

                    markerOptions1.rotation(mLastLocation.getBearing());
                    if (nearby_cab != null) {
                        nearby_cab.remove();
                    }


                    //  nearby_cab = mMap.addMarker(markerOptions1);

                    Marker nearby_cab1 = mMap.addMarker(markerOptions1);

                    //    mMap.addMarker(markerOptions1);
                    markers.add(nearby_cab1);

                    rotateMarker(nearby_cab1, -360, mMap);
                    Log.d("near_cab", "lop");

                    ///end map work
                }
            } else {

                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.car);
                Bitmap b = bitmapDrawable.getBitmap();
                Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);
                markerOptions1.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
                markerOptions1.rotation(mLastLocation.getBearing());

                AppUtil.topSnakBar(getActivity(), getActivity().getWindow().getDecorView().getRootView(), response_data.getString("message"));
            }
        } catch (Exception e) {
//          Toast.makeText(getApplicationContext(),e.toString(),Toast.LENGTH_LONG).show();
            Log.d("near_cab", e.getMessage());
        }
    }


    private String getDirectionsUrl(LatLng origin, LatLng dest) {
        Utility.log("MapTesting", "getDirectionsUrl");

        // Origin of route
        String str_origin = "origin=" + origin.latitude + "," + origin.longitude;

        // Destination of route
        String str_dest = "destination=" + dest.latitude + "," + dest.longitude;

        // Sensor enabled
        String sensor = "sensor=false";
        String key = "key=AIzaSyDRVBkjjZkrZf-_blL06aGAeQ2uSCuJRn8";

        String mode = "mode=driving";
        //transit
        String transit = "transit_routing_preference=less_driving";
        // Building the parameters to the web service
        String parameters = str_origin + "&" + str_dest + "&" + sensor + "&" + key + "&" + mode + "&" + transit;

        // Output format
        String output = "json";

        // Building the url to the web service
        // Building the url to the web service
        String url = "https://maps.googleapis.com/maps/api/directions/" + output + "?" + parameters;

        Log.d("result", url);
//my code
        // String url =   "http://www.yournavigation.org/api/1.0/gosmore.php?flat="+ origin.latitude+"&flon="+origin.longitude+"&tlat="+ dest.latitude +"&tlon="+ dest.longitude +"&format=geojson";


        //end my code

        return url;
    }

    /**
     * A method to download json data from url
     */
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
    @Override
    public void onResume() {
        super.onResume();
        showGpsSettingsAlert(getActivity());
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {

//        Log.d("types",object.toString());
        if (status) {
            try {
                JSONArray jsonArray = null;

                jsonArray = object.getJSONArray("result");

                for (int j = 0; j < jsonArray.length(); j++) {
                    JSONObject jsonObject = jsonArray.getJSONObject(j);
                    switch (j) {
                        case 0:
                            text_als.setText(jsonObject.getString("ambulanceType"));
                            break;
                        case 1:
                            text_bls.setText(jsonObject.getString("ambulanceType"));
                            break;
                        case 2:
                            text_dbt.setText(jsonObject.getString("ambulanceType"));
                            break;
                        case 3:
                            text_pvt.setText(jsonObject.getString("ambulanceType"));
                            break;

                    }

                }


            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    // Fetches data from url passed
    private class DownloadTask extends AsyncTask<String, Void, String> {
        boolean isBooked = false;

        public DownloadTask(boolean isBooked) {
            this.isBooked = isBooked;
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

        // Executes in UI thread, after the execution of
        // doInBackground()
        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);

            ParserTask parserTask = new ParserTask(isBooked);
            Log.d("result", result);
            // Invokes the thread for parsing the JSON data
            parserTask.execute(result);
        }
    }

    /**
     * A class to parse the Google Places in JSON format
     */
    private class ParserTask extends AsyncTask<String, Integer, List<List<HashMap<String, String>>>> {
        boolean isBooked = false;

        public ParserTask(boolean isBooked) {
            this.isBooked = isBooked;
        }

        // Parsing the data in non-ui thread
        @Override
        protected List<List<HashMap<String, String>>> doInBackground(String... jsonData) {

            JSONObject jObject;
            List<List<HashMap<String, String>>> routes = null;

            try {
                jObject = new JSONObject(jsonData[0]);

                Log.d("Background Task", jObject.toString());
                DirectionsJSONParser parser = new DirectionsJSONParser();
                //    PlaceJSONParserTemp parser = new   PlaceJSONParserTemp();
                // Starts parsing data
                routes = parser.parse(jObject);
            } catch (Exception e) {
                e.printStackTrace();
            }
            return routes;
        }

        // Executes in UI thread, after the parsing process
        @Override
        protected void onPostExecute(List<List<HashMap<String, String>>> result) {
            ArrayList<LatLng> points = null;
            PolylineOptions lineOptions = null;
            MarkerOptions markerOptions = new MarkerOptions();
            Log.d("Background Task new1", result.toString());
            // Traversing through all the routes
            for (int i = 0; i < result.size(); i++) {
                points = new ArrayList<LatLng>();
                lineOptions = new PolylineOptions();

                // Fetching i-th route
                List<HashMap<String, String>> path = result.get(i);


                // Fetching all the points in i-th route
                for (int j = 0; j < path.size(); j++) {
                    HashMap<String, String> point = path.get(j);

                    double lat = Double.parseDouble(point.get("lat"));
                    double lng = Double.parseDouble(point.get("lng"));
                    LatLng position = new LatLng(lat, lng);

                    points.add(position);


                }

                // Adding all the points in the route to LineOptions
                lineOptions.addAll(points);
                lineOptions.width(12);
                lineOptions.color(Color.YELLOW);
            }

            try {
                // Drawing polyline in the Google Map for the i-th route
                //    mMap.addPolyline(lineOptions);

                Log.d("Background after add", points.toString());

                final PolylineOptions finalLineOptions = lineOptions;
                final ArrayList<LatLng> finalPoints = points;
                getActivity().runOnUiThread(new Runnable() {
                    public void run() {
                        Log.d("UI thread", finalPoints.toString());
                        //my code
                        ArrayList<LatLng> pointss = new ArrayList<LatLng>();
                        PolylineOptions polyLineOptions = new PolylineOptions();

                        // traversing through routes
                        if (isBooked && ambMarker != null) {

                            pointss.add(ambMarker.getPosition());
                        } else {
                            pointss.add(source_location_marker.getPosition());
                        }

                        for (int i = 0; i < finalPoints.size(); i++)
                            pointss.add(finalPoints.get(i));
                        //  pointss.add(destination_location_marker.getPosition());
                        if (isBooked) {
                            pointss.add(source_location_marker.getPosition());
                        } else {
                            pointss.add(destination_location_marker.getPosition());
                        }
                        polyLineOptions.addAll(pointss);
                        polyLineOptions.width(10);
                        polyLineOptions.geodesic(true);

                        polyLineOptions.color(Color.RED);
                        if (isBooked) {
                            polyLineOptions.color(Color.BLUE);
                            if (driverPolyline != null) {
                                driverPolyline.remove();
                            }
                            driverPolyline = mMap.addPolyline(polyLineOptions);
                        } else {

                            if (polyline != null) {
                                polyline.remove();
                            }
                            polyline = mMap.addPolyline(polyLineOptions);
                        }

                        ///
                    }
                });


            } catch (Exception e) {
                // Do nothing
                Log.d("Background after ex", e.getMessage());
            }
        }
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */


    @Override
    public void onMapReady(GoogleMap googleMap) {

        try {
            Utility.log("MapTesting", "OnMapReady");
            boolean isSuccess = googleMap.setMapStyle(MapStyleOptions.loadRawResourceStyle(getActivity(), R.raw.uber_style_map));


        } catch (Exception e) {

            e.printStackTrace();
            Utility.log("MapTesting", "OnMapReadyExpection");
        }


        mMap = googleMap;
        // mMap.setMapType(GoogleMap.MAP_TYPE_NONE);
        mMap.getUiSettings().setRotateGesturesEnabled(false);
        mMap.getUiSettings().setMyLocationButtonEnabled(true);
        mMap.getUiSettings().setScrollGesturesEnabled(true);
        mMap.getUiSettings().setAllGesturesEnabled(true);

//        mMap.getUiSettings().setCompassEnabled(false);
//        mMap.getUiSettings().setMapToolbarEnabled(false);


//        mMap.getUiSettings().setScrollGesturesEnabled(false);
//        mMap.getUiSettings().setMyLocationButtonEnabled(false);


        //Initialize Google Play Services
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (ContextCompat.checkSelfPermission(getActivity(),
                    Manifest.permission.ACCESS_FINE_LOCATION)
                    == PackageManager.PERMISSION_GRANTED) {
                buildGoogleApiClient();
                mMap.setMyLocationEnabled(true);
                Utility.log("Lcoation", "OnActivityResult  ----LAtitude---InSide IFFF");
            }
        } else {
            buildGoogleApiClient();
            mMap.setMyLocationEnabled(true);
            Utility.log("Lcoation", "OnActivityResult  ----LAtitude---InSide Else");
        }
    }

    protected synchronized void buildGoogleApiClient() {
        mGoogleApiClient = new GoogleApiClient.Builder(getActivity())
                .addConnectionCallbacks(this)
                .addOnConnectionFailedListener(this)
                .addApi(LocationServices.API)
                .build();
        mGoogleApiClient.connect();
    }

    @Override
    public void onConnected(Bundle bundle) {

        mLocationRequest = new LocationRequest();
        mLocationRequest.setInterval(1000);
        mLocationRequest.setFastestInterval(1000);
        mLocationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);
        if (ContextCompat.checkSelfPermission(getActivity(),
                Manifest.permission.ACCESS_FINE_LOCATION)
                == PackageManager.PERMISSION_GRANTED) {
            LocationServices.FusedLocationApi.requestLocationUpdates(mGoogleApiClient, mLocationRequest, this);
        }
        mMap.setTrafficEnabled(false);
        mMap.animateCamera(CameraUpdateFactory.zoomTo(18));


//        mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(0, 0), 18.0f));
        mMap.setMyLocationEnabled(false);

    }

    @Override
    public void onConnectionSuspended(int i) {

    }

    @Override
    public void onLocationChanged(Location location) {
        Log.d("on location", location.getLatitude() + "");
        mLastLocation = location;
        Utility.log("MapTesting", "OnLoacationChangeistenerssssssssss");

        LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());

        if (!isSourceSet) {
            try {
                mMap.animateCamera(CameraUpdateFactory.zoomTo(18));

                Geocoder geocoder = new Geocoder(getActivity(), Locale.getDefault());
                List<Address> addresses = geocoder.getFromLocation(location.getLatitude(), location.getLongitude(), 1);
                String cityName = addresses.get(0).getAddressLine(0);
                String stateName = addresses.get(0).getAddressLine(1);
                source_location.setText(cityName + ", " + stateName);

                if (source_location_marker != null) {
                    source_location_marker.remove();
                }
                MarkerOptions markerOptions = new MarkerOptions();
                markerOptions.position(latLng);
                markerOptions.title("Source");

                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.marker_new);
                Bitmap b = bitmapDrawable.getBitmap();
                Bitmap smallCar = Bitmap.createScaledBitmap(b, 150, 81, false);

                markerOptions.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
                source_location_marker = mMap.addMarker(markerOptions);

//                CameraPosition cameraPosition = new CameraPosition.Builder()
//                        .target(latLng)      // Sets the center of the map to Mountain View
//                        .zoom(mMap.getCameraPosition().zoom)                   // Sets the zoom
//                        .bearing(location.getBearing())                // Sets the orientation of the camera to east
//                        .tilt(90)                   // Sets the tilt of the camera to 30 degrees
//                        .build();                   // Creates a CameraPosition from the builder
//                mMap.animateCamera(CameraUpdateFactory.newCameraPosition(cameraPosition));
                mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(source_location_marker.getPosition(), 15.0f));
                user_latlong = latLng;
                setNearbyCabsOnMap(latLng, userTypeId, ambulanceTypeId, ambulanceModeId);
                isSourceSet = true;
            } catch (Exception e) {
//                Toast.makeText(getApplication(), e.getMessage(), Toast.LENGTH_SHORT).show();
            }


        }

        if (tripStarted) {

            CameraPosition cameraPosition = new CameraPosition.Builder()
                    .target(latLng)      // Sets the center of the map to Mountain View
                    .zoom(mMap.getCameraPosition().zoom)                   // Sets the zoom
                    .bearing(location.getBearing())                // Sets the orientation of the camera to east
                    .tilt(90)                   // Sets the tilt of the camera to 30 degrees
                    .build();                   // Creates a CameraPosition from the builder
            mMap.animateCamera(CameraUpdateFactory.newCameraPosition(cameraPosition));

        }

    }


    @Override
    public void onConnectionFailed(ConnectionResult connectionResult) {

    }

    public static final int MY_PERMISSIONS_REQUEST_LOCATION = 99;

    public boolean checkLocationPermission() {
        if (ContextCompat.checkSelfPermission(getActivity(),
                Manifest.permission.ACCESS_FINE_LOCATION)
                != PackageManager.PERMISSION_GRANTED || ContextCompat.checkSelfPermission(getActivity(),
                Manifest.permission.CALL_PHONE)
                != PackageManager.PERMISSION_GRANTED) {

            // Asking user if explanation is needed
            if (ActivityCompat.shouldShowRequestPermissionRationale(getActivity(),
                    Manifest.permission.ACCESS_FINE_LOCATION) || ActivityCompat.shouldShowRequestPermissionRationale(getActivity(),
                    Manifest.permission.CALL_PHONE)) {

                // Show an explanation to the user *asynchronously* -- don't block
                // this thread waiting for the user's response! After the user
                // sees the explanation, try again to request the permission.

                //Prompt the user once explanation has been shown
                ActivityCompat.requestPermissions(getActivity(),
                        new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.CALL_PHONE},
                        MY_PERMISSIONS_REQUEST_LOCATION);


            } else {
                // No explanation needed, we can request the permission.
                ActivityCompat.requestPermissions(getActivity(),
                        new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.CALL_PHONE},
                        MY_PERMISSIONS_REQUEST_LOCATION);
            }
            return false;
        } else {
            return true;
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           String permissions[], int[] grantResults) {
        switch (requestCode) {
            case MY_PERMISSIONS_REQUEST_LOCATION: {
                // If request is cancelled, the result arrays are empty.
                if (grantResults.length > 0
                        && grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                    // permission was granted. Do the
                    // contacts-related task you need to do.
                    if (ContextCompat.checkSelfPermission(getActivity(),
                            Manifest.permission.ACCESS_FINE_LOCATION)
                            == PackageManager.PERMISSION_GRANTED) {

                        if (mGoogleApiClient == null) {
                            buildGoogleApiClient();
                        }
                        mMap.setMyLocationEnabled(true);
                    }

                } else {

                    // Permission denied, Disable the functionality that depends on this permission.
                    Toast.makeText(getActivity(), "permission denied", Toast.LENGTH_LONG).show();
                }
                return;
            }

            // other 'case' lines to check for other permissions this app might request.
            // You can add here other case statements according to your requirement.
        }
    }


    private void rotateMarker(final Marker mCurrent, final float i, GoogleMap mMap) {
        Utility.log("MapTesting", "OnRotateMarker");
        final Handler handler = new Handler();
        final long start = SystemClock.uptimeMillis();
        final float startRotation = mCurrent.getRotation();
        final long duration = 1500;
        final Interpolator interpolator = new LinearInterpolator();
        handler.post(new Runnable() {
            @Override
            public void run() {

                long elapsed = SystemClock.uptimeMillis() - start;
                float t = interpolator.getInterpolation((float) elapsed / duration);
                float rot = t * i + (1 - t) * startRotation;
                mCurrent.setRotation(-rot > 180 ? rot / 2 : rot);

                if (t < 1.0) {
                    handler.postDelayed(this, 16);


                }


            }
        });
    }


    private void setupUi(View view) {
        // set ambulance type
        Utility.log("MapTesting", "SetView");
        // Create the recyclerview.
        RecyclerView recyclerView = (RecyclerView) view.findViewById(R.id.rc_h);
        // Create the grid layout manager with 2 columns.
        GridLayoutManager layoutManager = new GridLayoutManager(getActivity(), 1);
        layoutManager.setOrientation(LinearLayoutManager.HORIZONTAL);
        //layoutManager.setOrientation(LinearLayoutManager.VERTICAL);

        // Set layout manager.
        recyclerView.setLayoutManager(layoutManager);
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("");
        arrayList.add("ewr");
        Horizontal_adapter horizontal_adapter = new Horizontal_adapter(getActivity(), arrayList);

        recyclerView.setAdapter(horizontal_adapter);


//        text_als= findViewById(R.id.text_als);
//        text_bls= findViewById(R.id.text_bls);
//        text_dbt= findViewById(R.id.text_dbt);
//        text_pvt= findViewById(R.id.text_pvt);
        this.myResult = this;

        //  Api_Calling.getMethodCall(MapsActivity.this, URLS.selectambulanceTypeMaster, getWindow().getDecorView().getRootView(),myResult,"show text",new JSONObject());

    }

    //mqtt

    private void addToHistory(String mainText) {

        Log.d("mqtt", mainText);
//        System.out.println("LOG: " + mainText);
//        mAdapter.add(mainText);
//        Snackbar.make(findViewById(android.R.id.content), mainText, Snackbar.LENGTH_LONG)
//                .setAction("Action", null).show();

    }

    public void subscribeToTopic(final String topic) {
        addToHistory("Subscribed! to topic" + topic);
        try {
            mqttAndroidClient.subscribe(topic, 0, null, new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    addToHistory("Subscribed! on topic" + topic);
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

        } catch (MqttException ex) {
            addToHistory("Exception whilst subscribing");
            ex.printStackTrace();
        }
    }

    public void publishMessage() {

        try {
            MqttMessage message = new MqttMessage();
            message.setPayload(publishMessage.getBytes());
            mqttAndroidClient.publish(publishTopic, message);
            addToHistory("Message Published");
            if (!mqttAndroidClient.isConnected()) {
                addToHistory(mqttAndroidClient.getBufferedMessageCount() + " messages in buffer.");
            }
        } catch (MqttException e) {
            System.err.println("Error Publishing: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public void mqttSetup() {
        //mqtt
        clientId = clientId + System.currentTimeMillis();
        try {
            mqttAndroidClient = new MqttAsyncClient(serverUri, clientId, null);
            mqttAndroidClient.setCallback(new MqttCallbackExtended() {
                @Override
                public void connectComplete(boolean reconnect, String serverURI) {

                    if (reconnect) {
                        addToHistory("Reconnected to : " + serverURI);
//                    // Because Clean Session is true, we need to re-subscribe
                        for (String topics : topiclist) {
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
                    addToHistory("Incoming message: o topic   " + topic + new String(message.getPayload()));
                    Log.d("mqtt:", "first" + DriverLocationTopic.equalsIgnoreCase(topic));
                    Utility.log("Arrievd_MQTTT", "" + message.toString() + "With Topic" + topic);
                    if (topic.equalsIgnoreCase(startRideTopic)) {
                        JSONObject jsonObject = new JSONObject(new String(message.getPayload()));
                        updateUiOnRideStart(jsonObject);
                    } else if (topic.equalsIgnoreCase(endRideTopic)) {
                        JSONObject jsonObject = new JSONObject(new String(message.getPayload()));
                        OnEndRidePopup(jsonObject);
                    } else if (topic.equalsIgnoreCase(bookTopic)) {
                        Log.d("mqtt:", "first1");
                        final JSONObject jsonObject = new JSONObject(new String(message.getPayload()));
                        getActivity().runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                Log.d("mqtt:", "first1");
                                updateUiOnBook(jsonObject);
                            }
                        });
                        Log.d("mqtt:", "first2");
                        if (!topiclist.contains(DriverLocationTopic)) {
                            Log.d("mqtt:", "first4");
                            topiclist.add(DriverLocationTopic);
                        }
                        subscribeToTopic(DriverLocationTopic);
                        Log.d("mqtt:", "first3");
                    } else if (topic.equalsIgnoreCase(DriverLocationTopic)) {
                        Log.d("mqtt9:", "second");
                        final JSONObject jsonObject = new JSONObject(new String(message.getPayload()));
                        try {
                            if (jsonObject != null) {
                                prevlocationAmb = ambulance_latlng;
                                ambulance_latlng = new LatLng(Double.parseDouble(jsonObject.getString("ambulanceLat")), Double.parseDouble(jsonObject.getString("ambulanceLng")));
                                Log.d("mqtt999:", "" + ambulance_latlng.latitude);
                            }

                        } catch (Exception e) {

                        }
                        getActivity().runOnUiThread(new Runnable() {
                            @Override
                            public void run() {

                                try {
                                    if (jsonObject != null) {

                                        Log.d("mqtt999:", "in ui" + ambulance_latlng.latitude);
                                        displayLocation();
                                    }

                                } catch (Exception e) {

                                }

                            }
                        });
                    }
                    subscribeToTopic(driverArriveTopic);
                    subscribeToTopic(startRideTopic);
                    subscribeToTopic(endRideTopic);
                    if (topic.equalsIgnoreCase(driverArriveTopic)) {
                        driverArrivedPopup(message.toString());
                        Utility.log("Arrievd MQTTT", "" + message.toString());

                    }
                }

                @Override
                public void deliveryComplete(IMqttDeliveryToken token) {

                }
            });
        } catch (MqttException e) {
            e.printStackTrace();

            Log.d("ccc", e.getMessage());
        }
        /////
    }
    public void coonectMqtt(final String topic) {


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
                    disconnectedBufferOptions.setBufferSize(500);

                    disconnectedBufferOptions.setPersistBuffer(false);
                    disconnectedBufferOptions.setDeleteOldestMessages(true);


                    mqttAndroidClient.setBufferOpts(disconnectedBufferOptions);
                    publishMessage();
                    subscribeToTopic(topic);
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    addToHistory("Failed to connect to: " + serverUri);
                    addToHistory("Failed to connect to: " + exception.getMessage());
                }
            });


        } catch (MqttException ex) {
            Log.d("mqtt:", ex.getMessage());
        }
    }

    //end
    public void updateUiOnBook(JSONObject response_data) {
        Log.d("mqtt:", "first41" + response_data.toString());
        try {
            if (response_data.getString("status").equals("true")) {
                if (nearby_cab != null) {
                    nearby_cab.remove();
                }
                for (Marker marker : markers) {
                    marker.remove();
                }
                //                        MarkerOptions markerOptions1=new MarkerOptions();
                JSONObject book_cab_response_data = response_data.getJSONObject("result");

                ride_id = AppUtil.getDatafromJSonObject(book_cab_response_data, "bookingId");


                bookingConfiramationPopup(ride_id);

                cab_no = AppUtil.getDatafromJSonObject(book_cab_response_data, "ambulanceNo");

                cab_id = AppUtil.getDatafromJSonObject(book_cab_response_data, "ambulanceId");


                driverId = AppUtil.getDatafromJSonObject(book_cab_response_data, "driverId");
                driver_name = AppUtil.getDatafromJSonObject(book_cab_response_data, "driverName");


                driver_phone = AppUtil.getDatafromJSonObject(book_cab_response_data, "driverMobile");

                driverLat = AppUtil.getDatafromJSonObject(book_cab_response_data, "ambulanceLat");
                drivetLng = AppUtil.getDatafromJSonObject(book_cab_response_data, "ambulanceLng");
                pickup_Lat = AppUtil.getDatafromJSonObject(book_cab_response_data, "pickupLatitude");
                pickup_long = AppUtil.getDatafromJSonObject(book_cab_response_data, "pickupLongitude");

                //otp = "OTP : " + book_cab_response_data.getString("otp");
                otp = "";


                fare = AppUtil.getDatafromJSonObject(book_cab_response_data, "finalAmount");


//                cab_no_a.setText(cab_no.split(" ")[0]);
//                cab_no_b.setText(cab_no.split(" ")[1]);
                cab_no_b.setText(cab_no);

                ride_driver_name.setText(driver_name);
                ride_otp.setText(otp);

                ride_fare.setText("RS " + fare);

                Log.d("book_ride", response_data.toString());
                ll_call.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Intent callIntent = new Intent(Intent.ACTION_CALL);
                        callIntent.setData(Uri.parse("tel:" + driver_phone));

                        if (ActivityCompat.checkSelfPermission(getActivity(),
                                Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED) {
                            return;
                        }
                        startActivity(callIntent);
                    }
                });


                ll_share.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Intent sharingIntent = new Intent(Intent.ACTION_SEND);
                        sharingIntent.setType("text/plain");
                        String shareBody = driver_name + " (" + driver_phone + ") is on the way in Cab number " + cab_no + ". You are paying " + fare + " for this ride. Share " + otp + " with the driver to start the ride.";
                        sharingIntent.putExtra(Intent.EXTRA_SUBJECT, "Near Cabs Booking");
                        sharingIntent.putExtra(Intent.EXTRA_TEXT, shareBody);
                        startActivity(Intent.createChooser(sharingIntent, "Share via"));
                    }
                });


                ll_cancel.setEnabled(true);
                ll_cancel.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        showCancelPopup(cab_id,ride_id,driverId);
                    }

                });

//
//                btnBookNow.setVisibility(View.GONE);
//                btnBookNow_layout.setVisibility(View.GONE);
                driver_info.setVisibility(View.VISIBLE);


                progressDialog.dismiss();

                MarkerOptions markerOptions1 = new MarkerOptions();


                prevlocationAmb = ambulance_latlng;
                ambulance_latlng = new LatLng(Double.parseDouble(driverLat), Double.parseDouble(drivetLng));
                markerOptions1.position(ambulance_latlng);

                BitmapDrawable bitmapDrawable;
                if (userTypeId.equalsIgnoreCase("1")) {
                    bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.amb);
                } else {
                    bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.responder);
                }
                Bitmap b = bitmapDrawable.getBitmap();
                Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);

                markerOptions1.icon(BitmapDescriptorFactory.fromBitmap(smallCar));

                markerOptions1.rotation(mLastLocation.getBearing());
                if (nearby_cab != null) {
                    nearby_cab.remove();
                }

                if (ambMarker != null) {
                    ambMarker.remove();
                }


                //  nearby_cab = mMap.addMarker(markerOptions1);

                ambMarker = mMap.addMarker(markerOptions1);

                //    mMap.addMarker(markerOptions1);
                //  markers.add(nearby_cab);

                rotateMarker(ambMarker, -360, mMap);
                Log.d("near_cab", "lop");

                if (!source_location.getText().toString().equals("") && !destination_location.getText().toString().equals("")) {
                    String url = getDirectionsUrl(ambMarker.getPosition(), source_location_marker.getPosition());
                    DownloadTask downloadTask = new DownloadTask(true);
                    // Start downloading json data from Google Directions API
                    downloadTask.execute(url);

                } else {

                }
                ///end map work


                //                        updateNearbyCabPosition();

                // handler.postDelayed(runnable, 0);
//                if(!topiclist.contains(DriverLocationTopic)){
//                    topiclist.add(DriverLocationTopic);
//                }
//
//
//                subscribeToTopic(DriverLocationTopic);


            } else {
                progressDialog.dismiss();
                Toast.makeText(getActivity(), response_data.getString("message"), Toast.LENGTH_LONG).show();
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }


    }

    private void updateUiOnDriverLocationChange(final JSONObject response_data) {
        Log.d("mqtt9:", "second6");

        try {
            if (response_data != null) {
                prevlocationAmb = ambulance_latlng;
                ambulance_latlng = new LatLng(Double.parseDouble(response_data.getString("ambulanceLat")), Double.parseDouble(response_data.getString("ambulanceLng")));
                displayLocation();
            }
//            String api_url = "https://nearcabs.000webhostapp.com/api/get_cab_location.php";
//
//            String get_cab_location_request = "cab_id=" + URLEncoder.encode(cab_id, "UTF-8") + "&ride_id=" + URLEncoder.encode(ride_id, "UTF-8");
//
//            JSONObject response_data = call_api(api_url, get_cab_location_request);

//                Toast.makeText(getApplicationContext(), response_data.toString(), Toast.LENGTH_LONG).show();

//            if (true) {
//
//                MapsActivity.this.runOnUiThread(new Runnable() {
//                    @Override
//                    public void run() {
//                        Log.d("mqtt9:","second55");
//                if (nearby_cab != null) {
//                    Log.d("mqtt9:","second44");
//                    nearby_cab.remove();
//                }}});
//
//                final MarkerOptions markerOptions1 = new MarkerOptions();
//                JSONObject get_cab_position_response_data = response_data;
//                   Log.d("fff",response_data.toString());
//
//                final LatLng nearby_cab_position = new LatLng(Double.parseDouble(get_cab_position_response_data.getString("ambulanceLat")), Double.parseDouble(get_cab_position_response_data.getString("ambulanceLng")));
//                markerOptions1.position(nearby_cab_position);
//
//                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.amb);
//                Bitmap b = bitmapDrawable.getBitmap();
//                Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);
//                markerOptions1.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
//                markerOptions1.title("ambulance");
//              //  markerOptions1.rotation(Float.parseFloat(get_cab_position_response_data.getString("cab_bearing")));
//                MapsActivity.this.runOnUiThread(new Runnable() {
//                    @Override
//                    public void run() {
//                        Log.d("mqtt99:","second65"+nearby_cab_position.latitude+"-"+nearby_cab_position.longitude);
//           nearby_cab = mMap.addMarker(markerOptions1);
//
//
//                    }});
//
//              //  handler.postDelayed(this, 10000);
//            } else if (response_data.getString("status").equals("2")) {
//                ll_cancel.setClickable(false);
//              //  handler.removeCallbacksAndMessages(runnable);
//                if (nearby_cab != null) {
//                    nearby_cab.remove();
//                }
//
//                tripStarted = true;
//               // cab.setVisibility(View.VISIBLE);
//            } else if (response_data.getString("status").equals("3")) {
//                ll_cancel.setClickable(false);
//               // handler.removeCallbacksAndMessages(runnable);
//            } else {
//                //handler.postDelayed(this, 10000);
//            }

        } catch (Exception e) {
            //handler.postDelayed(this, 10000);
            Log.d("mqtt9:", "second75");
            Log.d("mqtt9:", e.getMessage());
        }

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

    private void displayLocation() {

        Log.d("location", "display location");

        if (ActivityCompat.checkSelfPermission(getActivity(),
                Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(getActivity(),
                Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
        ) {

            return;
        }

        if (ambulance_latlng != null) {

            if (true) {

                final double lat = ambulance_latlng.latitude;
                final double lng = ambulance_latlng.longitude;

                Log.d("mqtt location:", lat + "-" + lng);


                if (prevlocationAmb == null || ambMarker == null) {
                    if (ambMarker != null) {
                        ambMarker.remove();
                    }
                    final MarkerOptions markerOptions = new MarkerOptions();

                    BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.amb);
                    Bitmap b = bitmapDrawable.getBitmap();
                    Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);

                    markerOptions.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
                    markerOptions.position(new LatLng(lat, lng));
                    markerOptions.title("ambulance");

                    ambMarker = mMap.addMarker(markerOptions);
                    mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(lat, lng), 15.0f));


                    Log.d("move", " no move car");

                } else {
                    Log.d("move", "move car");

                    movecar();
                }
                if (!source_location.getText().toString().equals("") && !destination_location.getText().toString().equals("")) {
                    String url = getDirectionsUrl(ambMarker.getPosition(), source_location_marker.getPosition());
                    DownloadTask downloadTask = new DownloadTask(true);

                    // Start downloading json data from Google Directions API
                    downloadTask.execute(url);


                } else {

                }
                if (prevlocationAmb != null) {

                    mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(lat, lng), 15.0f));
                    rotateMarker(ambMarker, (float) bearingBetweenLocations(prevlocationAmb, ambulance_latlng), mMap);

                }

//                if (mSrc!=null && mDest!=null && mCurrent!=null) {
//                    String url = getDirectionsUrl(mCurrent.getPosition(), mSrc.getPosition());
//                    String url1 = getDirectionsUrl(mSrc.getPosition(), mDest.getPosition());
////        DownloadTask downloadTask = new DownloadTask(false);
////
////           // Start downloading json data from Google Directions API
////           downloadTask.execute(url1);
//                   DownloadTask downloadTask1 = new DownloadTask(true);
//
//                    // Start downloading json data from Google Directions API
//                    downloadTask1.execute(url);
//                    //Animation
//
//
//
//
//                } else {
//
//                }


            }

        }
//       if(FPclient!=null){
//        FPclient.requestLocationUpdates(locationRequest,
//                new LocationCallback() {
//            @Override
//            public void onLocationResult(LocationResult locationResult) {
//                   Log.d("aaaaaasd",locationResult.toString());
////Get a reference to the database, so your app can perform read and write operations//
//                  location = locationResult.getLastLocation();.
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

    public void movecar() {
        final LatLng startPosition = prevlocationAmb;
        final LatLng finalPosition = ambulance_latlng;
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
                        startPosition.latitude * (1 - t) + finalPosition.latitude * t,
                        startPosition.longitude * (1 - t) + finalPosition.longitude * t);

                ambMarker.setPosition(currentPosition);
                Log.d("move.................", "move car");
                // Repeat till progress is complete.
                if (t < 1) {
                    // Post again 16ms later.
                    handler.postDelayed(this, 16);
                } else {
                    if (hideMarker) {
                        ambMarker.setVisible(false);
                    } else {
                        ambMarker.setVisible(true);

                    }
                }
            }
        });


    }

    private double bearingBetweenLocations(LatLng latLng1, LatLng latLng2) {

        double PI = 3.14159;
        double lat1 = latLng1.latitude * PI / 180;
        double long1 = latLng1.longitude * PI / 180;
        double lat2 = latLng2.latitude * PI / 180;
        double long2 = latLng2.longitude * PI / 180;

        double dLon = (long2 - long1);

        double y = Math.sin(dLon) * Math.cos(lat2);
        double x = Math.cos(lat1) * Math.sin(lat2) - Math.sin(lat1)
                * Math.cos(lat2) * Math.cos(dLon);

        double brng = Math.atan2(y, x);

        brng = Math.toDegrees(brng);
        brng = (brng + 360) % 360;

        return brng;
    }


//    public  void updateUiOnRideStart(JSONObject response_data){
//        Log.d("uuuuuuuuuuuuuu",""+ response_data.toString());
//        try {
//            if (response_data.getString("status").equals("true")) {
//                //                        MarkerOptions markerOptions1=new MarkerOptions();
//                JSONObject book_cab_response_data = response_data.getJSONObject("result");
//                Log.d("first41___AFTER_STA:","Inside"+ response_data.toString());
//
//
//
//
//
//
//                driverLat =AppUtil.getDatafromJSonObject(book_cab_response_data,"pickupLatitude");
//                drivetLng=AppUtil.getDatafromJSonObject(book_cab_response_data,"pickupLongitude");
//
//                pickup_Lat =AppUtil.getDatafromJSonObject(book_cab_response_data,"dropOffLatitude");
//                pickup_long=AppUtil.getDatafromJSonObject(book_cab_response_data,"dropOffLongitude");
//                Log.d("first41___AFTER_STA:","Above11111111111111111111111");
//
//
//
//
//
//
//                MarkerOptions markerOptions1 = new MarkerOptions();
//                ambulance_latlng = new LatLng(Double.parseDouble(driverLat), Double.parseDouble(drivetLng));
//                Log.d("first41___AFTER_STA:","Above222222222222222222222222222222");
//                markerOptions1.position(ambulance_latlng);
//                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.amb);
//                Bitmap b = bitmapDrawable.getBitmap();
//                Bitmap smallCar = Bitmap.createScaledBitmap(b, 60, 72, false);
//                markerOptions1.icon( BitmapDescriptorFactory.fromBitmap(smallCar));
//                Log.d("first41___AFTER_STA:","Above3333333333333333333333333333");
//
//                source_location_marker =   mMap.addMarker(markerOptions1);
//
//
//
//                Log.d("first41___AFTER_STA:","Above444444444444444444444444444444");
//
//
//
//                MarkerOptions markerOptions = new MarkerOptions();
//                dest_lating = new LatLng(Double.parseDouble(pickup_Lat), Double.parseDouble(pickup_long));
//                markerOptions.position(dest_lating);
//                BitmapDrawable bitmapDrawabl = (BitmapDrawable) getResources().getDrawable(R.drawable.marker);
//                Bitmap b1 = bitmapDrawabl.getBitmap();
//                Log.d("first41___AFTER_STA:","Above5555555555555555555555555555555");
//                Bitmap smallCar1 = Bitmap.createScaledBitmap(b1, 60, 72, false);
//                markerOptions.icon( BitmapDescriptorFactory.fromBitmap(smallCar1));
//                Log.d("first41___AFTER_STA:","Above666666666666666666666666666666666");
//                if(destination_location_marker!=null)
//                destination_location_marker =   mMap.addMarker(markerOptions);
//                Log.d("first41___AFTER_STA:","Above");
//                    String url = getDirectionsUrl(source_location_marker.getPosition() , destination_location_marker.getPosition());
//                    DownloadTask downloadTask = new DownloadTask(true);
//                    downloadTask.execute(url);
//                Log.d("first41___AFTER_STA:","Below");
//            } else {
//                Log.d("first41___AFTER_STA:","Else");
//                Toast.makeText(getActivity(), response_data.getString("message"), Toast.LENGTH_LONG).show();
//            }
//        } catch (JSONException e) {
//            e.printStackTrace();
//            Utility.log("first41___AFTER_STARTRIDERRRRRRRRRRRRRRRRR",""+e.getMessage());
//        }
//    }


    private void updateUiOnRideStart(final JSONObject jsonObject1) {
        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Utility.log("InsideMEtttttttttttt", "" + jsonObject1);
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject = jsonObject1.getJSONObject("result");
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                Log.d("InsideMEtttttttttttt", "" + jsonObject);
                try {
                    Log.d("InsideMEtttttttttttt", "!!!!!!!!!!!!!!!!!11");

                    Double srcLat = Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject, "pickupLatitude"));
                    Log.d("InsideMEtttttttttttt", "22222222222222222");
                    Double srcLng = Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject, "pickupLongitude"));
                    Log.d("InsideMEtttttttttttt", "22222222222222233333333333333333");
                    Double destLat = Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject, "dropOffLatitude"));
                    Log.d("InsideMEtttttttttttt", "!!!!!!!!!!!!!!!!!444444444444444444444");
                    Double destLng = Double.parseDouble(AppUtil.getDatafromJSonObject(jsonObject, "dropOffLongitude"));
                    Log.d("InsideMEtttttttttttt", "!!!!!!!!!!!!!!!!!155555555555555555");
                    LatLng destination_location = new LatLng(destLat, destLng);
                    Log.d("InsideMEtttttttttttt", "!!!!!!!!!!!!!!!!!116666666666666666666");
                    LatLng src_location = new LatLng(srcLat, srcLng);
                    Utility.log("InsideMEtttttttttttt", "" + destLat.toString());
                    Log.d("InsideMEtttttttttttt", "!!!!!!!!!!!!!!!!!17777777777777");
                    Utility.log("InsideMEtttttttttttt", "" + src_location.toString());
                    Log.d("InsideMEtttttttttttt", "!!!!!!!!!!!!!!!!!118888888888888888888");
                    MarkerOptions markerOptions = new MarkerOptions();
                    markerOptions.position(src_location);
                    markerOptions.title("Source");

                    BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.marker_new);
                    Bitmap b = bitmapDrawable.getBitmap();
                    Bitmap smallCar = Bitmap.createScaledBitmap(b, 150, 81, false);
                    markerOptions.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
//                markerOptions.rotation(location.getBearing());
                    Log.d("InsideMEtttttttttttt", "!!!!!!!!!!!!!!!999999999999999999999999");
                    ambMarker = mMap.addMarker(markerOptions);
                    if (ambMarker != null) {
                        ambMarker.remove();
                    }
                    MarkerOptions markerOptions1 = new MarkerOptions();
                    markerOptions1.position(destination_location);
                    markerOptions1.title("Destination");
                    BitmapDrawable bitmapDrawable1 = (BitmapDrawable) getResources().getDrawable(R.drawable.destination_marker);
                    Bitmap b1 = bitmapDrawable1.getBitmap();
                    Bitmap dest = Bitmap.createScaledBitmap(b1, 150, 81, false);

                    markerOptions1.icon(BitmapDescriptorFactory.fromBitmap(dest));
                    ///markerOptions.rotation(latLng.getBearing());
                    source_location_marker = mMap.addMarker(markerOptions1);
                    if (source_location_marker != null && ambMarker != null) {
//                String url = getDirectionsUrl(mCurrent.getPosition(), mSrc.getPosition());
                        String url1 = getDirectionsUrl(ambMarker.getPosition(), source_location_marker.getPosition());
                        BookYourRideFrgment.DownloadTask downloadTask = new BookYourRideFrgment.DownloadTask(true);
                        // Start downloading json data from Google Directions API
                        downloadTask.execute(url1);
//                DownloadTask downloadTask1 = new DownloadTask(true);
//                // Start downloading json data from Google Directions API
//                downloadTask1.execute(url);
                        //Animation
                    } else {

                    }

                } catch (Exception e) {
                    Log.d("set up ui on accept", "" + e);
                }

                Log.d("set up ui on accept", "" + "end");

            }
        });


    }


    public void noNearAmlumancePopup() {
        Utility.log("Inside", "MEthdei");
        final Dialog dialog;
        dialog = new Dialog(getActivity());
        dialog.setContentView(R.layout.logout_dialog_box);
        LinearLayout no = dialog.findViewById(R.id.no);
        LinearLayout yes = dialog.findViewById(R.id.yes);
        Atami_Bold msg = dialog.findViewById(R.id.lg);
        if (userTypeId.equalsIgnoreCase("2")) {
            msg.setText("You have no near Responder");
        } else {
            msg.setText("You have no near Ambulance");
        }
        Atami_Regular yestext = dialog.findViewById(R.id.yestext);
        yestext.setText("Ok");
        dialog.getWindow().addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK);
        dialog.setCanceledOnTouchOutside(false);
        no.setVisibility(View.GONE);
        int Width = (int) (getResources().getDisplayMetrics().widthPixels * 0.95);
        int Height = (int) (getResources().getDisplayMetrics().heightPixels * 0.60);
        dialog.show();
        dialog.getWindow().setLayout(Width, Height);
        yes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dialog.dismiss();
            }
        });
        no.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dialog.dismiss();
            }
        });
        progressDialog.dismiss();
    }


    public void OnEndRidePopup(final JSONObject jsonObject) {
        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Utility.log("Inside", "MEthdei---"+jsonObject);

                Intent intent=new Intent(getContext(), End_Ride_Activity.class);
                try {
                    Gson gson= new GsonBuilder().create();
                    EndRideModel model= gson.fromJson(jsonObject.getString("result"), new TypeToken<EndRideModel>(){}.getType());
                    intent.putExtra("data",model);
                    getContext().startActivity(intent);
                } catch (JSONException e) {
                    e.printStackTrace();
                }


//                final Dialog dialog;
//                dialog = new Dialog(getActivity());
//                dialog.setContentView(R.layout.new_end_ride_popup);
//                LinearLayout no = dialog.findViewById(R.id.no);
//                LinearLayout yes = dialog.findViewById(R.id.yes);
//                Atami_Bold msg = dialog.findViewById(R.id.lg);
//                Atami_Regular yestext = dialog.findViewById(R.id.yestext);
//                yestext.setText("Ok");
//                dialog.getWindow().addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK);
//                dialog.setCanceledOnTouchOutside(false);
//                int Width = (int) (getResources().getDisplayMetrics().widthPixels * 0.95);
//                int Height = (int) (getResources().getDisplayMetrics().heightPixels * 0.60);
//                dialog.show();
//                dialog.getWindow().setLayout(Width, Height);
//                yes.setOnClickListener(new View.OnClickListener() {
//                    @Override
//                    public void onClick(View v) {
//                        dialog.dismiss();
//                        mMap.clear();
//                    }
//                });
//                no.setOnClickListener(new View.OnClickListener() {
//                    @Override
//                    public void onClick(View v) {
//                        dialog.dismiss();
//                        mMap.clear();
//                    }
//                });
            }
        });

    }


    public void bookingConfiramationPopup(final String bookingId) {
        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                final Dialog dialog;
                dialog = new Dialog(getActivity());
                dialog.setContentView(R.layout.layout_booking_confirm);
                LinearLayout yes = dialog.findViewById(R.id.track);
                Atami_Bold btnText = dialog.findViewById(R.id.btnText);
                if (userTypeId.equalsIgnoreCase("2"))
                    btnText.setText("Track Responder");
                dialog.getWindow().addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK);
                dialog.setCanceledOnTouchOutside(false);
                Atami_Regular bookingid = dialog.findViewById(R.id.bokingid);
                int Width = (int) (getResources().getDisplayMetrics().widthPixels * 1);
                int Height = (int) (getResources().getDisplayMetrics().heightPixels * 1);
                dialog.show();
                bookingid.setText("Booking ID " + bookingId);
                dialog.getWindow().setLayout(Width, Height);
                yes.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        dialog.dismiss();
                    }
                });
            }
        });

    }


    public void driverArrivedPopup(final String data) {
        Utility.log("InsideMEthod", "" + data);
        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                final Dialog dialog;
                dialog = new Dialog(getActivity());
                dialog.setContentView(R.layout.driver_arrived_popup);
                LinearLayout yes = dialog.findViewById(R.id.track);
                Atami_Regular msg = dialog.findViewById(R.id.bokingid);
                if (userTypeId.equalsIgnoreCase("1")) {
                    msg.setText("Driver Arrived");
                } else {
                    msg.setText("Responder Arrived");
                }
                dialog.getWindow().addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK);
                dialog.setCanceledOnTouchOutside(false);
                int Width = (int) (getResources().getDisplayMetrics().widthPixels * 1);
                int Height = (int) (getResources().getDisplayMetrics().heightPixels * .50);
                dialog.show();
                dialog.getWindow().setLayout(Width, Height);
                yes.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        dialog.dismiss();
                    }
                });
            }
        });

    }


    private void showBottomLayout(final String modelKey) {
        selection_layout.setVisibility(View.GONE);
        bottomlayout.setVisibility(View.VISIBLE);
        ALS.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNearbyCabsOnMap(user_latlong, "1", "1", modelKey);
                location_field_layout.setVisibility(View.VISIBLE);
                bottomlayout.setVisibility(View.GONE);
            }
        });
        BLS.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNearbyCabsOnMap(user_latlong, "1", "2", modelKey);
                location_field_layout.setVisibility(View.VISIBLE);
                bottomlayout.setVisibility(View.GONE);
            }
        });
        DBT.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNearbyCabsOnMap(user_latlong, "1", "4", modelKey);
                bottomlayout.setVisibility(View.GONE);
                location_field_layout.setVisibility(View.VISIBLE);
            }
        });
        PVT.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNearbyCabsOnMap(user_latlong, "1", "3", modelKey);
                location_field_layout.setVisibility(View.VISIBLE);
                bottomlayout.setVisibility(View.GONE);
            }
        });
        AIR.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
            }
        });
    }

    private void showCancelPopup(final String ambulanceId, final String bookingId, final String driverId) {
        Questionid="";
        Utility.log("Show", "ShowCancelPopup");
        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                final Dialog dialog;
                dialog = new Dialog(getActivity());
                dialog.setContentView(R.layout.cancelbookinglayout);
                Button yes = dialog.findViewById(R.id.yes);
                Button no = dialog.findViewById(R.id.no);
                final ListView listView = dialog.findViewById(R.id.list);
                listView.setAdapter(new CustomAdapter(questionModelArrayList, getContext()));
                dialog.setCancelable(false);
                int Width = (int) (getResources().getDisplayMetrics().widthPixels * 1);
                int Height = (int) (getResources().getDisplayMetrics().heightPixels * .60);
                dialog.getWindow().setLayout(Width, Height);
                no.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        dialog.dismiss();
                    }
                });
                yes.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        if(!Questionid.equalsIgnoreCase("")){
                        dialog.dismiss();
                        if (userTypeId.equalsIgnoreCase("1")) {
                            try {
                                String cancel_api_url =base_url+"cancelRide";
                                JSONObject jsonObject=new JSONObject();
                                progressDialog.setTitle("Processing...");
                                progressDialog.show();
                                jsonObject.put("ambulanceId",""+ambulanceId).put("bookingId",""+bookingId).put("userId",""+sharedPreferences.getUserId()).put("questionId",""+Questionid).put("driverId",""+driverId);
                                JSONObject cancel_response_data = call_api(cancel_api_url, jsonObject.toString());
                                Utility.log("CancelRideJSOn","---"+jsonObject.toString());
                                Utility.log("CancelRide",""+cancel_response_data.toString());
                                if (cancel_response_data.getString("status").equals("true")) {
                                    Toast.makeText(getActivity(), "Booking Cancelled", Toast.LENGTH_SHORT).show();
                                    driver_info.setVisibility(View.GONE);
                                    btnBookNow.setVisibility(View.VISIBLE);
                                    mMap.clear();
                                    showGpsSettingsAlert(getActivity());
                                    btnBookNow_layout.setVisibility(View.VISIBLE);
                                    progressDialog.dismiss();
                                }else {
                                    progressDialog.dismiss();
                                }
                            } catch (Exception e) {
                                //                                 Toast.makeText(getApplicationContext(), e.getMessage(), Toast.LENGTH_SHORT).show();
                            }
                        } else {
                            try {
                                progressDialog.setTitle("Processing...");
                                progressDialog.show();
                                String cancel_api_url =base_url+"cancelResponder";
                                JSONObject jsonObject=new JSONObject();
                                jsonObject.put("ambulanceId",""+ambulanceId).put("bookingId",""+bookingId).put("userId",""+sharedPreferences.getUserId()).put("questionId",""+Questionid).put("driverId",""+driverId);
                                JSONObject cancel_response_data = call_api(cancel_api_url, jsonObject.toString());
                                Utility.log("CancelRide",""+cancel_response_data.toString());
                                if (cancel_response_data.getString("status").equals("true")) {
                                    Toast.makeText(getActivity(), "Booking Cancelled", Toast.LENGTH_SHORT).show();
                                    driver_info.setVisibility(View.GONE);
                                    btnBookNow.setVisibility(View.VISIBLE);
                                    mMap.clear();
                                    showGpsSettingsAlert(getActivity());
                                    btnBookNow_layout.setVisibility(View.VISIBLE);
                                    progressDialog.dismiss();
                                }else {
                                    progressDialog.dismiss();
                                }
                            } catch (Exception e) {//                                 Toast.makeText(getApplicationContext(), e.getMessage(), Toast.LENGTH_SHORT).show();
                            }
                        }}else {
//                            Utility.topSnakBar(getActivity(),getActivity().getWindow().getDecorView().getRootView(),"Please select any one option");
                            Toast.makeText(getContext(), "Please select any one option", Toast.LENGTH_SHORT).show();
                        }
                    }
                });
                dialog.show();// Create a List from String Array elements

            }
        });
    }
    private  void ApiCalling()
    {
        JsonObjectRequest jsonObjectRequest=new JsonObjectRequest(Request.Method.POST, URLS.allcancelquestions, null, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {

                Utility.log("Cancel_Response",""+response.toString());
                try {
                    if(Boolean.parseBoolean(response.getString("status")))
                    {
                      Gson gson= new GsonBuilder().create();
                    ArrayList<QuestionModel> rm = gson.fromJson(response.getString("result"), new TypeToken<ArrayList<QuestionModel>>(){}.getType());
                      questionModelArrayList.clear();
                      questionModelArrayList.addAll(rm);
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Utility.log("Cancel_Response","---"+error.getMessage());
            }
        });
        RequestQueue requestQueue= Volley.newRequestQueue(getContext());
        requestQueue.add(jsonObjectRequest);
    }

    @Override
    public void onStart() {
        super.onStart();
        ApiCalling();
    }

    public class CustomAdapter extends ArrayAdapter<QuestionModel>{

        private ArrayList<QuestionModel> dataSet;
        Context mContext;
        int Counter=-1;


        // View lookup cache
        private  class ViewHolder {
            TextView txtName;
        }

        public CustomAdapter(ArrayList<QuestionModel> data, Context context) {
            super(context, R.layout.singlelayout, data);
            this.dataSet = data;
            this.mContext=context;

        }
        private int lastPosition = -1;

        @Override
        public View getView(final int position, View convertView, ViewGroup parent) {
            // Get the data item for this position
            final QuestionModel dataModel = getItem(position);
            // Check if an existing view is being reused, otherwise inflate the view
            ViewHolder viewHolder; // view lookup cache stored in tag

            final View result;

            if (convertView == null) {

                viewHolder = new ViewHolder();
                LayoutInflater inflater = LayoutInflater.from(getContext());
                convertView = inflater.inflate(R.layout.singlelayout, parent, false);
                viewHolder.txtName = (TextView) convertView.findViewById(R.id.text);
                result=convertView;
                convertView.setTag(viewHolder);
            } else {
                viewHolder = (ViewHolder) convertView.getTag();
                result=convertView;
            }
            lastPosition = position;
            viewHolder.txtName.setText(dataModel.getQuestions());
            final View finalConvertView = convertView;
            final View finalConvertView1 = convertView;
            convertView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Counter=position;
                    Questionid=dataModel.getQuestionsId();
                    notifyDataSetChanged();
                    Utility.log("DDDDD","---"+dataModel.getQuestionsId());
                }
            });
//            for (int i=0;i<dataSet.size();i++)
//            {
                if(position==Counter)
                {
                    finalConvertView.setBackgroundColor(Color.RED);
                }else {
                    finalConvertView1.setBackgroundColor(Color.WHITE);
                }
//            }
            // Return the completed view to render on screen
            return convertView;
        }
    }

}

