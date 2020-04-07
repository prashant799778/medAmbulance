package com.example.respondermedambulance.Activity;

import android.Manifest;
import android.content.pm.PackageManager;
import android.location.Location;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;

import androidx.core.content.ContextCompat;
import androidx.fragment.app.FragmentActivity;

import com.example.respondermedambulance.Api_Calling.MyResult;
import com.example.respondermedambulance.Api_Calling.current_location;
import com.example.respondermedambulance.Comman.Api_Calling;
import com.example.respondermedambulance.Comman.URLS;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_Regular;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.LocationListener;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class BookAmbulance extends FragmentActivity implements OnMapReadyCallback, current_location,MyResult {

    private GoogleMap mMap;
    Atami_Regular text_als,text_bls,text_dbt,text_pvt;
    MyResult myResult;
    Location mLastLocation;
    Marker mCurrLocationMarker;
    GoogleApiClient mGoogleApiClient;
    private LocationRequest mLocationRequest;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.book_ambulance_activity);

        text_als= findViewById(R.id.text_als);
        text_bls= findViewById(R.id.text_bls);
        text_dbt= findViewById(R.id.text_dbt);
        text_pvt= findViewById(R.id.text_pvt);

        this.myResult=this;

        Api_Calling.getMethodCall(BookAmbulance.this, URLS.selectambulanceMaster, getWindow().getDecorView().getRootView(),myResult,"show text",showText());

        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    private Object showText() {
        JSONObject jsonObject=new JSONObject();

        return jsonObject;
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        // Add a marker in Sydney and move the camera
        if (android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (ContextCompat.checkSelfPermission(this,
                    Manifest.permission.ACCESS_FINE_LOCATION)
                    == PackageManager.PERMISSION_GRANTED) {
                buildGoogleApiClient();
                mMap.setMyLocationEnabled(true);
            }
        }
        else {
            buildGoogleApiClient();
            mMap.setMyLocationEnabled(true);
        }
    }

    protected synchronized void buildGoogleApiClient() {
        mGoogleApiClient = new GoogleApiClient.Builder(this)
                .addConnectionCallbacks((GoogleApiClient.ConnectionCallbacks) this)
                .addOnConnectionFailedListener((GoogleApiClient.OnConnectionFailedListener) this)
                .addApi(LocationServices.API).build();
        mGoogleApiClient.connect();


    }


    @Override
    public void onConnected(Bundle bundle) {

        mLocationRequest = new LocationRequest();
        mLocationRequest.setInterval(1000);
        mLocationRequest.setFastestInterval(1000);
        mLocationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);
        if (ContextCompat.checkSelfPermission(this,
                Manifest.permission.ACCESS_FINE_LOCATION)
                == PackageManager.PERMISSION_GRANTED) {
            LocationServices.FusedLocationApi.requestLocationUpdates(mGoogleApiClient, mLocationRequest, (LocationListener) this);
        }

    }



    @Override
    public void onLocationChanged(Location location) {

        mLastLocation = location;
        if (mCurrLocationMarker != null) {
            mCurrLocationMarker.remove();
        }
        //Place current location marker
        LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());
        MarkerOptions markerOptions = new MarkerOptions();
        markerOptions.position(latLng);
        markerOptions.title("Current Position");
        markerOptions.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_GREEN));
        mCurrLocationMarker = mMap.addMarker(markerOptions);

        //move map camera
        mMap.moveCamera(CameraUpdateFactory.newLatLng(latLng));
        mMap.animateCamera(CameraUpdateFactory.zoomTo(11));

        //stop location updates
        if (mGoogleApiClient != null) {
            LocationServices.FusedLocationApi.removeLocationUpdates(mGoogleApiClient, (LocationListener) this);
        }

    }


    @Override
    public void onConnectionFailed(ConnectionResult connectionResult) {

    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
Log.d("asd",object.toString());
        if(status){     try {
            JSONArray jsonArray= null;

                jsonArray = object.getJSONArray("result");

            for(int j=0;j<jsonArray.length();j++){
               JSONObject jsonObject= jsonArray.getJSONObject(j);
                 switch (j){
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
}
