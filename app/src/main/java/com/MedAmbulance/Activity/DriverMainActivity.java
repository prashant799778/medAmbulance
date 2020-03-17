package com.MedAmbulance.Activity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.ListView;

import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.fragment.app.FragmentManager;

import com.MedAmbulance.Activity.ui.home.HomeFragment;
import com.MedAmbulance.Adapters.DrawerI_Adapter;
import com.MedAmbulance.Adapters.DrawerModel;
import com.MedAmbulance.Fragments.MyTrip_fragment;
import com.MedAmbulance.Fragments.Myprofile_Fragment;
import com.MedAmbulance.Fragments.Notifucation_fragment;
import com.MedAmbulance.R;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

public class DriverMainActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    ListView listView;
    DrawerLayout drawerLayout;
    ImageView openDrawer;
    ActionBarDrawerToggle actionBarDrawerToggle;


    @SuppressLint("WrongViewCast")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver_main);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map_driver);
        mapFragment.getMapAsync(this);


        listView = findViewById(R.id.driver_list_view);
        openDrawer=findViewById(R.id.openDrawer);
        drawerLayout = findViewById(R.id.drawerlayut);

        openDrawer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // If navigation drawer is not open yet, open it else close it.
                drawerLayout.addDrawerListener(actionBarDrawerToggle);
                if(!drawerLayout.isDrawerOpen(GravityCompat.START)) drawerLayout.openDrawer(Gravity.LEFT);
                else drawerLayout.closeDrawer(Gravity.LEFT);
            }
        });


        DrawerModel[] drawerItem = new DrawerModel[6];
        drawerItem[0] = new DrawerModel(R.drawable.taxi, "Home");
        drawerItem[1] = new DrawerModel(R.drawable.ic_home, "My Profile");
        drawerItem[2] = new DrawerModel(R.drawable.rate_card,"My Trips");
        drawerItem[3] = new DrawerModel(R.drawable.ic_bell, "Notifications");
        drawerItem[4] = new DrawerModel(R.drawable.about, "Online Support");
        drawerItem[5] = new DrawerModel(R.drawable.logout, "Logout");

        DrawerI_Adapter adapter = new DrawerI_Adapter(this, R.layout.drawer_list_view, drawerItem);
        listView.setOnItemClickListener(new DrawerItemClickListener());
        listView.setAdapter(adapter);
        // set default fragment here
        selectItem(0);

    }

    public class DrawerItemClickListener implements AdapterView.OnItemClickListener {
        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            selectItem(position);

        }
    }

    private void selectItem(int position) {


        Fragment fragment = null;


        switch (position)
        {   case 0:
            fragment = new HomeFragment();
            drawerLayout.closeDrawers();
            break;

            case 1:
                fragment = new Myprofile_Fragment();
                drawerLayout.closeDrawers();
                break;

            case 2:
                fragment = new MyTrip_fragment();
                drawerLayout.closeDrawers();
                break;
            case 3:
                fragment = new Notifucation_fragment();
                drawerLayout.closeDrawers();
                break;
            case 4:
                startActivity(new Intent(DriverMainActivity.this, SupportActivity.class));

                drawerLayout.closeDrawers();
                break;
            case 5:
                drawerLayout.closeDrawers();
                break;

        }
        if (fragment != null) {
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction().replace(R.id.map_driver, fragment).commit();

            listView.setItemChecked(position, true);
            listView.setSelection(position);

        } else {
            Log.e("MainActivity", "Error in creating fragment");
        }
    }



    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        // Add a marker in Sydney and move the camera
        LatLng sydney = new LatLng(-34, 151);
        mMap.addMarker(new MarkerOptions().position(sydney).title("Marker in Sydney"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(sydney));
    }
}
