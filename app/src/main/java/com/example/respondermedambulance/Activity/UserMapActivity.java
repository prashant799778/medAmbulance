package com.example.respondermedambulance.Activity;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.app.AlertDialog;
import android.app.Dialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.location.Address;
import android.location.Location;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.Settings;

import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.AutoCompleteTextView;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.SimpleAdapter;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.fragment.app.FragmentManager;

import com.example.respondermedambulance.R;
import com.example.respondermedambulance.cognalys.CheckNetworkConnection;
import com.example.respondermedambulance.cognalys.GPSTracker;
import com.example.respondermedambulance.rangebar.RangeBar;
import com.example.respondermedambulance.util.AppUtil;
import com.example.respondermedambulance.util.GData;
import com.example.respondermedambulance.util.GetLocationAsyncTask;
import com.example.respondermedambulance.util.PlaceJSONParser;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
import com.google.android.gms.common.GooglePlayServicesRepairableException;
import com.google.android.gms.common.GooglePlayServicesUtil;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.GoogleApiClient.ConnectionCallbacks;
import com.google.android.gms.common.api.GoogleApiClient.OnConnectionFailedListener;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.location.places.Place;
import com.google.android.gms.location.places.ui.PlacePicker;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.GoogleMap.OnCameraChangeListener;
import com.google.android.gms.maps.GoogleMap.OnMarkerDragListener;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.CameraPosition;
import com.google.android.gms.maps.model.Circle;
import com.google.android.gms.maps.model.CircleOptions;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.maps.model.PolylineOptions;
import com.shivtechs.maplocationpicker.LocationPickerActivity;
import com.shivtechs.maplocationpicker.MapUtility;


/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 *

 */
public class  UserMapActivity  extends TLTBaseActivity implements OnClickListener, OnMarkerDragListener, ConnectionCallbacks, OnConnectionFailedListener, GetLocationAsyncTask.LocationReceivedListener
{
    /** The Constant TAG. */
    private static final String TAG = UserMapActivity.class.getSimpleName();
    private static final int ADDRESS_PICKER_REQUEST = 90;
    private ImageButton btnClose;
    private RangeBar _radiusRangeBar;
    private TextView _tvRadius;
    private GPSTracker gpsTracker;
    private SupportMapFragment serviceAreaMapFragment;
    private GoogleMap serviceAreaMap;
    private static final double DEFAULT_RADIUS = 1000;
    private double myRadius = 1000;
    public static final double RADIUS_OF_EARTH_METERS = 6371009;
    private Circle circle;
    private Marker centerMarker;
    private List<DraggableCircle> mCircles = new ArrayList<DraggableCircle>(1);

    private LocationRequest mLocationRequest;
    boolean mUpdatesRequested = false;
    // Google client to interact with Google API
    private GoogleApiClient mGoogleApiClient;
    private LatLng center;
    private LatLng to;
    private AutoCompleteTextView autoCompleteHomeAddress;
    private ParserTask parserTask;
    private PlacesTask placesTask;
    private EditText etZipcode;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_map);

        MapUtility.apiKey = getResources().getString(R.string.MAP_SERVER_API_KEY);



//		etAddress = (EditText)findViewById(R.id.etAddress);
        etZipcode = (EditText)findViewById(R.id.etZipCode);
        autoCompleteHomeAddress = (AutoCompleteTextView)findViewById(R.id.autoCompHomeAddress);
        btnClose = (ImageButton)findViewById(R.id.btnClose);
        btnClose.setOnClickListener(this);
        FragmentManager fm = getSupportFragmentManager();
        serviceAreaMapFragment = (SupportMapFragment) fm.findFragmentById(R.id.serviceAreaMap);


        _radiusRangeBar = (RangeBar)findViewById(R.id.rangebar1);
        _tvRadius = (TextView)findViewById(R.id.tvRadious);
        _radiusRangeBar.setSeekPinByIndex(1);
        _radiusRangeBar.setOnRangeBarChangeListener(new RangeBar.OnRangeBarChangeListener()
        {
            @Override
            public void onRangeChangeListener(RangeBar rangeBar, int leftPinIndex,int rightPinIndex, String leftPinValue, String rightPinValue)
            {
                AppUtil.LogMsg(TAG, "Left pin Value"+leftPinValue+"  Right Pin Value:- "+rightPinValue+" Right Pin Index:- "+rightPinIndex);
                _tvRadius.setText(rightPinValue+" KM");
                if(circle!=null)
                {
                    myRadius = rightPinIndex*DEFAULT_RADIUS;
                    circle.setRadius(rightPinIndex*DEFAULT_RADIUS);
                }
            }
        });

        autoCompleteHomeAddress.setThreshold(1);
        autoCompleteHomeAddress.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                PlacePicker.IntentBuilder builder = new PlacePicker.IntentBuilder();
                try {
                    // for activty
                    startActivityForResult(builder.build(UserMapActivity.this), ADDRESS_PICKER_REQUEST);
                    // for fragment
                    //startActivityForResult(builder.build(getActivity()), PLACE_PICKER_REQUEST);
                } catch (GooglePlayServicesRepairableException e) {
                    e.printStackTrace();
                } catch (GooglePlayServicesNotAvailableException e) {
                    e.printStackTrace();
                }
            }
        });
//        autoCompleteHomeAddress.addTextChangedListener(new TextWatcher()
//        {
//            @Override
//            public void onTextChanged(CharSequence s, int start, int before, int count)
//            {
//
//
//
////            Intent i = new Intent(UserMapActivity.this, LocationPickerActivity.class);
////                startActivityForResult(i, ADDRESS_PICKER_REQUEST);
////                if (gpsTracker.canGetLocation())
////                {
////                    placesTask = new PlacesTask();
////                    placesTask.execute(s.toString());
////                }
//
//
//            }
//
//            @Override
//            public void beforeTextChanged(CharSequence s, int start, int count, int after)
//            {
//                // TODO Auto-generated method stub
//            }
//
//            @Override
//            public void afterTextChanged(Editable s)
//            {
//                // TODO Auto-generated method stub
//            }
//        });
    }

    protected synchronized void buildGoogleApiClient()
    {
        mGoogleApiClient = new GoogleApiClient.Builder(this)
                .addConnectionCallbacks(this)
                .addOnConnectionFailedListener(this)
                .addApi(LocationServices.API).build();
    }
    private void zoomToMyLocation(GoogleMap googleMap, Location location)
    {
        if (location != null)
        {
            if(googleMap != null)
            {
                googleMap.clear();
            }

            centerMarker = googleMap.addMarker(new MarkerOptions()
                    .position(new LatLng(location.getLatitude(), location.getLongitude()))
                    .draggable(false));

            CameraPosition cameraPosition = new CameraPosition.Builder()
                    .target(new LatLng(location.getLatitude(), location.getLongitude()))      // Sets the center of the map to location user
                    .zoom(15.0f)                // Sets the zoom
                    .bearing(90)                // Sets the orientation of the camera to east
                    .tilt(40)                   // Sets the tilt of the camera to 30 degrees
                    .build();                   // Creates a CameraPosition from the builder


            DraggableCircle circle = new DraggableCircle(new LatLng(location.getLatitude(), location.getLongitude()), DEFAULT_RADIUS);
            mCircles.add(circle);

            googleMap.animateCamera(CameraUpdateFactory.newCameraPosition(cameraPosition));
        }
    }


    @Override
    protected void onResume()
    {
        super.onResume();
        gpsTracker = new GPSTracker(this);
        if(gpsTracker.canGetLocation())
        {
            if (serviceAreaMap == null)
            {
                serviceAreaMapFragment.getMapAsync(new OnMapReadyCallback() {
                    @Override
                    public void onMapReady(GoogleMap googleMap) {
                        serviceAreaMap = googleMap;
                        serviceAreaMap.setOnMarkerDragListener(UserMapActivity.this);
                        setupLocation();
                        if (CheckNetworkConnection.isConnectionAvailable(getApplicationContext()))
                        {
                            if (gpsTracker.canGetLocation())
                            {
                                Location location = gpsTracker.getLocation();
                                zoomToMyLocation(serviceAreaMap, location);
                            }
                        }

                        serviceAreaMap.setMyLocationEnabled(true);
                        serviceAreaMap.setOnCameraChangeListener(new OnCameraChangeListener()
                        {
                            @Override
                            public void onCameraChange(CameraPosition arg0)
                            {
                                center = serviceAreaMap.getCameraPosition().target;
                                serviceAreaMap.clear();
                                mCircles.clear();
                                DraggableCircle circle = new DraggableCircle(new LatLng(center.latitude, center.longitude), DEFAULT_RADIUS);
                                mCircles.add(circle);
                                centerMarker = serviceAreaMap.addMarker(new MarkerOptions()
                                        .position(new LatLng(center.latitude, center.longitude))
                                        .draggable(false));
                                if(to!=null){

                                    serviceAreaMap.addMarker(new MarkerOptions()
                                            .position(new LatLng(to.latitude, to.longitude))
                                            .draggable(false));
                                    PolylineOptions polyLineOptions =new PolylineOptions();
                                    ArrayList<LatLng> points = new ArrayList<LatLng>();

                                    // traversing through routes
                                    points.add(center);
                                    points.add(to);

                                    polyLineOptions.addAll(points);
                                    polyLineOptions.width(10);
                                    polyLineOptions.color(Color.BLUE);


                                    serviceAreaMap.addPolyline(polyLineOptions);
                                }


                                try
                                {
                                    if (CheckNetworkConnection.isConnectionAvailable(getApplicationContext()))
                                    {
                                        if (gpsTracker.canGetLocation())
                                        {
//									GetLocationAsyncTask getLocation = new GetLocationAsyncTask(ServiceAreaActivityNew.this, center.latitude, center.longitude);
//									getLocation.setListener(ServiceAreaActivityNew.this);
//									getLocation.execute();
                                        }
                                    }
                                }
                                catch (Exception e)
                                {
                                    AppUtil.LogMsg(TAG, e.toString());
                                }
                            }
                        });
                    }
                });

            }


        }
        else
        {
            showGpsSettingsAlert();
        }
    }

    @Override
    public void onClick(View v)
    {
        switch (v.getId())
        {
//            case R.id.btnSaveRateCard:
////			callUpdateApi();
//                break;
//
//            default:
//                break;
        }
    }

    @Override
    public void onMarkerDrag(Marker marker)
    {
        onMarkerMoved(marker);
    }

    @Override
    public void onMarkerDragEnd(Marker marker)
    {
        onMarkerMoved(marker);
    }

    @Override
    public void onMarkerDragStart(Marker marker)
    {
        onMarkerMoved(marker);
    }

    private class DraggableCircle
    {
        private double radius;
        public DraggableCircle(LatLng center, double radius) {
            this.radius = radius;
            circle = serviceAreaMap.addCircle(new CircleOptions()
                    .center(center)
                    .radius(radius)
                    .strokeWidth(1)
                    .strokeColor(Color.parseColor("#501e88e5"))
                    .fillColor(Color.parseColor("#501277d0")));
        }
        public boolean onMarkerMoved(Marker marker)
        {
            if (marker.equals(centerMarker)) {
                circle.setCenter(marker.getPosition());
                return true;
            }
            return false;
        }
    }

    /** Generate LatLng of radius marker */
    private static LatLng toRadiusLatLng(LatLng center, double radius) {
        double radiusAngle = Math.toDegrees(radius / RADIUS_OF_EARTH_METERS) /
                Math.cos(Math.toRadians(center.latitude));
        return new LatLng(center.latitude, center.longitude + radiusAngle);
    }

    private static double toRadiusMeters(LatLng center, LatLng radius) {
        float[] result = new float[1];
        Location.distanceBetween(center.latitude, center.longitude,
                radius.latitude, radius.longitude, result);
        return result[0];
    }

    private void onMarkerMoved(Marker marker)
    {
        for (DraggableCircle draggableCircle : mCircles)
        {
            if (draggableCircle.onMarkerMoved(marker))
            {
                break;
            }
        }
    }

    @Override
    public void onConnected(Bundle arg0)
    {

    }

    @Override
    public void onConnectionSuspended(int arg0)
    {

    }

    @Override
    public void onConnectionFailed(ConnectionResult arg0)
    {

    }

    @Override
    public void onAddressReceived(Address address)
    {

    }


    /** A method to download json data from url */
    private String downloadUrl(String strUrl) throws IOException{
        String data = "";
        InputStream iStream = null;
        HttpURLConnection urlConnection = null;
        try{
            AppUtil.LogMsg("Downloading Map Data", strUrl);
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
            while( ( line = br.readLine()) != null){
                sb.append(line);
            }

            data = sb.toString();

            br.close();

        }catch(Exception e){
            AppUtil.LogException(e);
        }finally{
            iStream.close();
            urlConnection.disconnect();
        }
        return data;
    }
    // Fetches all places from GooglePlaces AutoComplete Web Service
    private class PlacesTask extends AsyncTask<String, Void, String>
    {
        @Override
        protected String doInBackground(String... place)
        {
            // For storing data from web service
            String data = "";

            // Obtain browser key from https://code.google.com/apis/console
            String key = "key="+getResources().getString(R.string.MAP_SERVER_API_KEY);

            String input="";

            try {
                input = "input=" + URLEncoder.encode(place[0], "utf-8");
            } catch (UnsupportedEncodingException e1) {
                e1.printStackTrace();
            }

            // place type to be searched
            String types = "types=geocode";

            // Sensor enabled
            String sensor = "sensor=false";

            // Building the parameters to the web service
            String parameters = input+"&"+types+"&"+sensor+"&"+key;

            // Output format
            String output = "json";

            // Building the url to the web service
            String url = "https://maps.googleapis.com/maps/api/place/autocomplete/"+output+"?"+parameters;

            try{
                // Fetching the data from we service
                data = downloadUrl(url);
            }catch(Exception e){
                AppUtil.LogMsg("Background Task",e.toString());
            }
            return data;
        }

        @Override
        protected void onPostExecute(String result)
        {
            super.onPostExecute(result);
            // Creating ParserTask
            parserTask = new ParserTask();
            // Starting Parsing the JSON string returned by Web Service
            parserTask.execute(result);
        }
    }


    /** A class to parse the Google Places in JSON format */
    private class ParserTask extends AsyncTask<String, Integer, List<HashMap<String,String>>>{

        JSONObject jObject;

        @Override
        protected List<HashMap<String, String>> doInBackground(String... jsonData) {

            List<HashMap<String, String>> places = null;

            PlaceJSONParser placeJsonParser = new PlaceJSONParser();

            try
            {
                jObject = new JSONObject(jsonData[0]);
                places = placeJsonParser.parse(jObject);

            }catch(Exception e){
                AppUtil.LogException(e);
            }
            return places;
        }

        @Override
        protected void onPostExecute(List<HashMap<String, String>> result) {

            String[] from = new String[] { "description"};
            int[] to = new int[] { android.R.id.text1 };

            // Creating a SimpleAdapter for the AutoCompleteTextView
            SimpleAdapter adapter = new SimpleAdapter(UserMapActivity.this, result, android.R.layout.simple_list_item_1, from, to);
            // Setting the adapter
            autoCompleteHomeAddress.setAdapter(adapter);
            autoCompleteHomeAddress.setOnItemClickListener(new OnItemClickListener()
            {
                @Override
                public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                    // Get data associated with the specified position
                    // in the list (AdapterView)
                    Map description = (Map) parent.getItemAtPosition(position);
                    String address = description.get("description").toString();
                    autoCompleteHomeAddress.setText(address);
                    new GeocoderTask().execute(address);
                }
            });
        }
    }

    /** A class to parse the Google Places in JSON format */
    private class GeocoderTask extends AsyncTask<String, Void, String>{

        JSONObject jObject;

        @Override
        protected String doInBackground(String... place) {

            String data = "";

            // Obtain browser key from https://code.google.com/apis/console
            String key = "key="+getResources().getString(R.string.MAP_SERVER_API_KEY);

            String input="";

            try {
                input = "address=" + URLEncoder.encode(place[0], "utf-8");
            } catch (UnsupportedEncodingException e1) {
                e1.printStackTrace();
            }


            // Sensor enabled
            String sensor = "sensor=false";

            // Building the parameters to the web service
            String parameters = input+"&"+sensor+"&"+key;

            // Output format
            String output = "json";

            // Building the url to the web service
            String url = "https://maps.googleapis.com/maps/api/geocode/"+output+"?"+parameters;

            try
            {
                // Fetching the data from we service
                data = downloadUrl(url);
            }catch(Exception e){
                AppUtil.LogException(e);
            }
            return data;
        }

        @Override
        protected void onPostExecute(String result)
        {
            AppUtil.LogMsg("GEOCODINGGGGG  ",result);
            try
            {
                JSONObject jobj = new JSONObject(result);
                JSONArray jobj1 = jobj.getJSONArray("results");
                JSONObject jobj2 = jobj1.getJSONObject(0);
                JSONObject jobj3 = jobj2.getJSONObject("geometry");
                JSONObject jobj4 = jobj3.getJSONObject("location");
                Location targetLocation = new Location("");//provider name is unecessary
                targetLocation.setLatitude(jobj4.getDouble("lat"));//your coords of course
                targetLocation.setLongitude(jobj4.getDouble("lng"));
                zoomToMyLocation(serviceAreaMap, targetLocation);
                if (CheckNetworkConnection.isConnectionAvailable(getApplicationContext()))
                {
                    if (gpsTracker.canGetLocation())
                    {
                        GetLocationAsyncTask getLocation = new GetLocationAsyncTask(UserMapActivity.this, center.latitude, center.longitude);
                        getLocation.setListener(UserMapActivity.this);
                        getLocation.execute();
                    }
                }
            }
            catch (JSONException e)
            {
                e.printStackTrace();
            }

        }
    }


    private void setupLocation()
    {
        int status = GooglePlayServicesUtil.isGooglePlayServicesAvailable(getBaseContext());

        if (status != ConnectionResult.SUCCESS)
        { // Google Play Services are
            // not available
            int requestCode = 10;
            Dialog dialog = GooglePlayServicesUtil.getErrorDialog(status, this,requestCode);
            dialog.show();
        }
        else
        {
            buildGoogleApiClient();
            if (mGoogleApiClient != null)
            {
                mGoogleApiClient.connect();
            }
            // Getting reference to the SupportMapFragment
            // Create a new global location parameters object
            mLocationRequest = LocationRequest.create();
            /*
             * Set the update interval
             */
            mLocationRequest.setInterval(GData.UPDATE_INTERVAL_IN_MILLISECONDS);

            // Use high accuracy
            mLocationRequest.setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY);

            // Set the interval ceiling to one minute
            mLocationRequest.setFastestInterval(GData.FAST_INTERVAL_CEILING_IN_MILLISECONDS);

            // Note that location updates are off until the user turns them on
            mUpdatesRequested = false;

            /*
             * Create a new location client, using the enclosing class to handle
             * callbacks.
             */
        }
    }


    public void showGpsSettingsAlert()
    {
        AlertDialog.Builder alertDialog = new AlertDialog.Builder(this);

        //Setting Dialog Title
        alertDialog.setTitle(R.string.app_name);

        //Setting Dialog Message
        alertDialog.setMessage(R.string.GPSAlertDialogMessage);

        //On Pressing Setting button
        alertDialog.setPositiveButton(R.string.settings, new DialogInterface.OnClickListener()
        {
            @Override
            public void onClick(DialogInterface dialog, int which)
            {
                Intent intent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
                startActivity(intent);
            }
        });

        //On pressing cancel button
        alertDialog.setNegativeButton(R.string.cancel, new DialogInterface.OnClickListener()
        {
            @Override
            public void onClick(DialogInterface dialog, int which)
            {
                dialog.cancel();
                finish();
            }
        });

        alertDialog.show();
    }


//    @Override
//    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
//        super.onActivityResult(requestCode, resultCode, data);
//        if (requestCode == ADDRESS_PICKER_REQUEST) {
//            try {
//                if (data != null && data.getStringExtra(MapUtility.ADDRESS) != null) {
//                    String address = data.getStringExtra(MapUtility.ADDRESS);
//                    double selectedLatitude = data.getDoubleExtra(MapUtility.LATITUDE, 0.0);
//                    double selectedLongitude = data.getDoubleExtra(MapUtility.LONGITUDE, 0.0);
//                    autoCompleteHomeAddress.setText("Address: "+address);
//                   // txtLatLong.setText("Lat:"+selectedLatitude+"  Long:"+selectedLongitude);
//                }
//            } catch (Exception ex) {
//                ex.printStackTrace();
//            }
//        }
//    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);


        if (resultCode == RESULT_OK) {
            switch (requestCode){
                case ADDRESS_PICKER_REQUEST:
                    Place place = PlacePicker.getPlace(this, data);
                    String placeName = String.format("Place: %s", place.getName());
                    double latitude = place.getLatLng().latitude;
                    double longitude = place.getLatLng().longitude;
                    autoCompleteHomeAddress.setText(placeName);
                    serviceAreaMap.addMarker(new MarkerOptions()
                            .position(new LatLng(latitude,longitude))
                            .draggable(false));

                    ArrayList<LatLng> points = new ArrayList<LatLng>();
                    PolylineOptions polyLineOptions =new PolylineOptions();

                    // traversing through routes
                    points.add(center);
                    points.add(new LatLng(latitude,longitude));

                        polyLineOptions.addAll(points);
                        polyLineOptions.width(10);
                        polyLineOptions.color(Color.BLUE);

                       to=new LatLng(latitude,longitude);
                    serviceAreaMap.addPolyline(polyLineOptions);


            }
        }
    }


}
