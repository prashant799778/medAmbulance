package com.MedAmbulance.Activity;


import android.Manifest;
import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.graphics.drawable.BitmapDrawable;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.StrictMode;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.fragment.app.FragmentManager;

import com.MedAmbulance.Adapters.DrawerI_Adapter;
import com.MedAmbulance.Adapters.DrawerModel;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Fragments.BookYourRideFrgment;
import com.MedAmbulance.Fragments.Myprofile_Fragment;
import com.MedAmbulance.Fragments.RateCardFragment;
import com.MedAmbulance.Fragments.YourRidesFragment;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;
import com.MedAmbulance.util.AppUtil;
import com.MedAmbulance.util.PlaceJSONParserTemp;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
import com.google.android.gms.common.GooglePlayServicesRepairableException;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.LocationCallback;
import com.google.android.gms.location.LocationListener;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationResult;
import com.google.android.gms.location.LocationServices;
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
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.maps.model.PolylineOptions;

import org.json.JSONArray;
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
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Timer;

public class MapsActivity extends FragmentActivity implements  MyResult {
    Dialog dialog;
    int flag = 0;
    boolean isSourceSet = false, tripStarted = false;
    ListView listView;

    Atami_Regular header, user_phone_no;
    public Atami_Bold user_name;

    EditText source_location, destination_location;
    Myprofile_Fragment myprofile_fragment;
    String TAG = "LocationSelect";
    int AUTOCOMPLETE_SOURCE = 1, AUTOCOMPLETE_DESTINATITON = 2;
    GoogleMap mMap;

    //textView
    Atami_Regular text_als, text_bls, text_dbt, text_pvt;

    //DrawerLayout
    DrawerLayout drawerLayout;
    ImageView opernDrawer;
    LinearLayout openUserProfile;
    ActionBarDrawerToggle actionBarDrawerToggle;


    MyResult myResult;
    GoogleApiClient mGoogleApiClient;
    Location mLastLocation;

    Marker mCurrLocationMarker;
    static Marker source_location_marker;
    static Marker destination_location_marker;
    Marker nearby_cab;
    LocationRequest mLocationRequest;
    ArrayList<LatLng> markerPoints;
    Button btnBookNow;
    ImageView cab;
    BookYourRideFrgment bookmyridefragment;
    RelativeLayout driver_info;
    LinearLayout ll_call, ll_share, ll_cancel, btnBookNow_layout;
    String driver_name, cab_no, cab_id, otp, fare, driver_phone, ride_id;
    TextView cab_no_a, cab_no_b, ride_otp, ride_driver_name, ride_fare;
    String PREFS_NAME = "auth_info";
    ProgressDialog progressDialog;
    Timer timer;
    Handler handler;
    MySharedPrefrence m;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        Animatoo.animateSlideLeft(MapsActivity.this);
        bookmyridefragment = new BookYourRideFrgment();
        myprofile_fragment = new Myprofile_Fragment();
        m = MySharedPrefrence.instanceOf(getApplicationContext());
        user_phone_no = findViewById(R.id.user_phone_no);
        user_name = findViewById(R.id.user_name);
        text_als = findViewById(R.id.text_als);
        text_bls = findViewById(R.id.text_bls);
        text_dbt = findViewById(R.id.text_dbt);
        text_pvt = findViewById(R.id.text_pvt);
        header = findViewById(R.id.farg_name);
        listView = findViewById(R.id.left_drawer);


        opernDrawer = findViewById(R.id.openDrawer);
        m.setLoggedIn(true);
        m.setUserTypeId("2");
        FragmentManager fragmentManager = getSupportFragmentManager();
        fragmentManager.beginTransaction().replace(R.id.map, bookmyridefragment).commit();
        header.setText("Book Your Rides");
        opernDrawer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                drawerLayout = findViewById(R.id.drawerlayut);
                // If navigation drawer is not open yet, open it else close it.
                drawerLayout.addDrawerListener(actionBarDrawerToggle);
                if (!drawerLayout.isDrawerOpen(GravityCompat.START))
                    drawerLayout.openDrawer(Gravity.LEFT);
                else drawerLayout.closeDrawer(Gravity.LEFT);
            }
        });
        DrawerModel[] drawerItem = new DrawerModel[6];
        drawerItem[0] = new DrawerModel(R.drawable.taxi, "Book Your Ride");
        drawerItem[1] = new DrawerModel(R.drawable.your_ride, "My Ride");
        drawerItem[2] = new DrawerModel(R.drawable.rate_card, "Rate Card");
        drawerItem[3] = new DrawerModel(R.drawable.support, "Support");
        drawerItem[4] = new DrawerModel(R.drawable.about, "About");
        drawerItem[5] = new DrawerModel(R.drawable.logout, "Logout");


        DrawerI_Adapter adapter = new DrawerI_Adapter(this, R.layout.drawer_list_view, drawerItem);
        listView.setOnItemClickListener(new DrawerItemClickListener());
        listView.setAdapter(adapter);


        this.myResult = this;

//        Api_Calling.getMethodCall(MapsActivity.this, URLS.selectambulanceMaster, getWindow().getDecorView().getRootView(), myResult, "show text", showText());
        handler = new Handler();
        driver_info = (RelativeLayout) findViewById(R.id.driver_details);
        driver_info.setVisibility(View.GONE);


        progressDialog = new ProgressDialog(this);
        progressDialog.setMessage("Booking...");
        progressDialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);
        progressDialog.setIndeterminate(true);
        progressDialog.setProgress(0);
        progressDialog.setCancelable(false);

        ll_call = (LinearLayout) findViewById(R.id.ll_call);
        ll_share = (LinearLayout) findViewById(R.id.ll_share);
        ll_cancel = (LinearLayout) findViewById(R.id.ll_cancel);

        cab_no_a = (TextView) findViewById(R.id.cab_no_a);
        cab_no_b = (TextView) findViewById(R.id.cab_no_b);
        ride_driver_name = (TextView) findViewById(R.id.driver_name);
        ride_otp = (TextView) findViewById(R.id.ride_otp);
        ride_fare = (TextView) findViewById(R.id.ride_fare);

        openUserProfile = findViewById(R.id.goto_profile);
        openUserProfile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FragmentManager fragmentManager = getSupportFragmentManager();
                fragmentManager.beginTransaction().replace(R.id.map, myprofile_fragment).commit();
                header.setText("My Profile");
                drawerLayout.closeDrawers();
            }
        });

        btnBookNow_layout = (LinearLayout) findViewById(R.id.btnBookNow_layout);
        btnBookNow = (Button) findViewById(R.id.btnBookNow);
        btnBookNow.setVisibility(View.GONE);
        btnBookNow_layout.setVisibility(View.GONE);


        cab = (ImageView) findViewById(R.id.ambulance);
        cab.setVisibility(View.GONE);
        timer = new Timer();
        markerPoints = new ArrayList<LatLng>();
        StrictMode.ThreadPolicy threadPolicy = new StrictMode.ThreadPolicy.Builder().build();
        StrictMode.setThreadPolicy(threadPolicy);

        source_location = (EditText) findViewById(R.id.source_location);
        destination_location = (EditText) findViewById(R.id.destination_location);
    }



    @Override
    public void onResult(JSONObject object, Boolean status) {


        Log.d("asd", object.toString());
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



    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(MapsActivity.this);
        if(bookmyridefragment.isVisible() && bookmyridefragment!=null)
        {
            Utility.log("ffffffffffffffffff","ffffffffffffffffffffff");
           finishAffinity();
        }else {
            Utility.log("EEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEE");
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction().replace(R.id.map, bookmyridefragment).commit();
            header.setText("Book Your Rides");
        }
    }
    private class DrawerItemClickListener implements AdapterView.OnItemClickListener {
        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            selectItem(position);

        }
    }

    private void selectItem(int position) {


        Fragment fragment = null;


        switch (position) {
            case 0:
                fragment = new BookYourRideFrgment();
                header.setText("Book Your Ride");
                drawerLayout.closeDrawers();
                break;

            case 1:
                fragment = new YourRidesFragment();
                header.setText("Your Rides");
                drawerLayout.closeDrawers();
                break;

            case 2:
                fragment = new RateCardFragment();
                header.setText("Rate Card");
                drawerLayout.closeDrawers();
                break;
            case 3:
                startActivity(new Intent(MapsActivity.this, SupportActivity.class));
                drawerLayout.closeDrawers();
                break;
            case 4:
                startActivity(new Intent(MapsActivity.this, AboutActivity.class));
                drawerLayout.closeDrawers();
                break;
            case 5:
                dialog = new Dialog(MapsActivity.this);
                dialog.setContentView(R.layout.logout_dialog_box);
                LinearLayout no=dialog.findViewById(R.id.no);
                LinearLayout yes=dialog.findViewById(R.id.yes);
                dialog.getWindow().addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP |Intent.FLAG_ACTIVITY_NEW_TASK );
                dialog.setCanceledOnTouchOutside(false);
                int Width =(int) (getResources().getDisplayMetrics().widthPixels*0.95);
                int Height =(int) (getResources().getDisplayMetrics().heightPixels*0.60);
                dialog.show();
                dialog.getWindow().setLayout(Width,Height);
                drawerLayout.closeDrawers();
                yes.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        m.setLoggedIn(false);
                        m.clearData();
                        dialog.dismiss();
                        startActivity(new Intent(MapsActivity.this,Countinue_As_Acrtivity.class));
                        finish();
                    }
                });
                no.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                      dialog.dismiss();
                    }
                });
                break;

        }
        if (fragment != null) {
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction().replace(R.id.map, fragment).commit();
            listView.setItemChecked(position, true);
            listView.setSelection(position);

        } else {
            Log.e("MainActivity", "Error in creating fragment");
        }
    }

    @Override
    protected void onStart() {
        super.onStart();
        user_phone_no.setText(m.getMobile());
        user_name.setText(m.getname());

    }
}
