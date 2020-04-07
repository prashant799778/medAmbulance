package com.example.drivermedambulance.Fragments;

import android.Manifest;
import android.content.Context;
import android.content.IntentSender;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Handler;
import android.os.StrictMode;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.example.drivermedambulance.Activity.MapsActivity;
import com.example.drivermedambulance.Adapters.Horizontal_adapter;
import com.example.drivermedambulance.Api_Calling.MyResult;
import com.example.drivermedambulance.Comman.MySharedPrefrence;
import com.example.drivermedambulance.R;
import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
import com.google.android.gms.common.GooglePlayServicesRepairableException;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.PendingResult;
import com.google.android.gms.common.api.ResultCallback;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.location.LocationSettingsRequest;
import com.google.android.gms.location.LocationSettingsResult;
import com.google.android.gms.location.LocationSettingsStatusCodes;
import com.google.android.gms.location.places.ui.PlacePicker;
import com.google.android.gms.maps.model.LatLng;

import org.json.JSONObject;

import java.util.ArrayList;
import java.util.Timer;

public class BookRide extends Fragment implements MyResult {
    String TAG = "LocationSelect";
    MySharedPrefrence sharedPrefrence;
    Handler handler;
    RelativeLayout driver_info;
    LinearLayout ll_call, ll_share, ll_cancel, btnBookNow_layout;
    TextView cab_no_a, cab_no_b, ride_otp, ride_driver_name, ride_fare;
    Button btnBookNow;
    ImageView cab;
    Timer timer;
    ArrayList<LatLng> markerPoints;
    EditText source_location, destination_location;
    MyResult myResult;
    RecyclerView recyclerView;

    public static final int MY_PERMISSIONS_REQUEST_LOCATION = 99;
    private static final int REQUEST_CHECK_SETTINGS = 93;
    int AUTOCOMPLETE_SOURCE = 1, AUTOCOMPLETE_DESTINATITON = 2;

    OnBookRideListener listener;

    public BookRide() {
        // Required empty public constructor
    }

    public static BookRide newInstance() {
        BookRide fragment = new BookRide();
        Bundle args = new Bundle();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_user_book_your_ride, container, false);
        sharedPrefrence = MySharedPrefrence.instanceOf(getContext());

        onFindViewById(view); // set ID for the component
        handler = new Handler();
        timer = new Timer();

        driver_info.setVisibility(View.GONE); // hide driver layout
        btnBookNow.setVisibility(View.GONE);
        btnBookNow_layout.setVisibility(View.GONE);
        cab.setVisibility(View.GONE);

        markerPoints = new ArrayList<LatLng>();

        StrictMode.ThreadPolicy threadPolicy = new StrictMode.ThreadPolicy.Builder().build();
        StrictMode.setThreadPolicy(threadPolicy);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            checkLocationPermission();
        }
        setupUi();

        source_location.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               listener.picUpLocation();
            }
        });

        return view;
    }

    private void onFindViewById(View view) {
        driver_info = (RelativeLayout) view.findViewById(R.id.driver_details);
        ll_call = (LinearLayout) view.findViewById(R.id.ll_call);
        ll_share = (LinearLayout) view.findViewById(R.id.ll_share);
        ll_cancel = (LinearLayout) view.findViewById(R.id.ll_cancel);

        cab_no_a = (TextView) view.findViewById(R.id.cab_no_a);
        cab_no_b = (TextView) view.findViewById(R.id.cab_no_b);
        ride_driver_name = (TextView) view.findViewById(R.id.driver_name);
        ride_otp = (TextView) view.findViewById(R.id.ride_otp);
        ride_fare = (TextView) view.findViewById(R.id.ride_fare);

        btnBookNow_layout = (LinearLayout) view.findViewById(R.id.btnBookNow_layout);
        btnBookNow = (Button) view.findViewById(R.id.btnBookNow);

        cab = (ImageView) view.findViewById(R.id.ambulance);
        source_location = (EditText) view.findViewById(R.id.source_location);
        destination_location = (EditText) view.findViewById(R.id.destination_location);
        recyclerView = (RecyclerView) view.findViewById(R.id.rc_h);
    }

    public boolean checkLocationPermission() {
        if (ContextCompat.checkSelfPermission(getContext(),
                Manifest.permission.ACCESS_FINE_LOCATION)
                != PackageManager.PERMISSION_GRANTED || ContextCompat.checkSelfPermission(getContext(),
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
    public void onResume() {
        super.onResume();
        showGpsSettingsAlert(getActivity());
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

    private void setupUi() {
        // set ambulance type
        // Create the recyclerview.
        // Create the grid layout manager with 2 columns.
        GridLayoutManager layoutManager = new GridLayoutManager(getContext(), 1);
        layoutManager.setOrientation(LinearLayoutManager.HORIZONTAL);
        //layoutManager.setOrientation(LinearLayoutManager.VERTICAL);

        // Set layout manager.
        recyclerView.setLayoutManager(layoutManager);
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("");
        arrayList.add("ewr");
        Horizontal_adapter horizontal_adapter = new Horizontal_adapter(getContext(), arrayList);

        recyclerView.setAdapter(horizontal_adapter);

//        text_als= findViewById(R.id.text_als);
//        text_bls= findViewById(R.id.text_bls);
//        text_dbt= findViewById(R.id.text_dbt);
//        text_pvt= findViewById(R.id.text_pvt);
        this.myResult = this;
        //  Api_Calling.getMethodCall(MapsActivity.this, URLS.selectambulanceTypeMaster, getWindow().getDecorView().getRootView(),myResult,"show text",new JSONObject());

    }


    @Override
    public void onResult(JSONObject object, Boolean status) {

    }

    @Override
    public void onAttach(@NonNull Context context) {
        super.onAttach(context);
        if (context instanceof OnBookRideListener){
            this.listener = (OnBookRideListener) context;
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
    }

    public interface OnBookRideListener {
        public void picUpLocation();
    }
}
