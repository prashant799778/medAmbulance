package com.example.respondermedambulance.Activity;
//
//import androidx.appcompat.app.ActionBarDrawerToggle;
//import androidx.core.view.GravityCompat;
//import androidx.drawerlayout.widget.DrawerLayout;
//import androidx.fragment.app.Fragment;
//import androidx.fragment.app.FragmentActivity;
//import androidx.fragment.app.FragmentManager;
//
//import android.app.AlertDialog;
//import android.content.DialogInterface;
//import android.content.Intent;
//import android.graphics.Bitmap;
//import android.graphics.drawable.BitmapDrawable;
//import android.os.Bundle;
//import android.util.Log;
//import android.view.Gravity;
//import android.view.View;
//import android.widget.AdapterView;
//import android.widget.ImageView;
//import android.widget.ListView;
//
//import com.example.respondermedambulance.Activity.ui.AboutUs;
//import com.example.respondermedambulance.Activity.ui.Support_Us;
//import com.example.respondermedambulance.Activity.ui.Your_Rides;
//import com.example.respondermedambulance.Adapters.DrawerI_Adapter;
//import com.example.respondermedambulance.Adapters.DrawerModel;
//import com.example.respondermedambulance.Comman.MySharedPrefrence;
//import com.example.respondermedambulance.Fragments.BookRide;
//import com.example.respondermedambulance.Fragments.RateCardFragment;
//import com.example.respondermedambulance.Fragments.UserBookYourRideFragment;
//import com.example.respondermedambulance.R;
//import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
//import com.google.android.gms.common.GooglePlayServicesRepairableException;
//import com.google.android.gms.common.api.Status;
//import com.google.android.gms.location.places.Place;
//import com.google.android.gms.location.places.ui.PlaceAutocomplete;
//import com.google.android.gms.location.places.ui.PlacePicker;
//import com.google.android.gms.maps.CameraUpdateFactory;
//import com.google.android.gms.maps.model.BitmapDescriptorFactory;
//import com.google.android.gms.maps.model.LatLng;
//import com.google.android.gms.maps.model.MarkerOptions;
//
public class UserModuleActivity {

}
        //extends FragmentActivity implements BookRide.OnBookRideListener {
//
//    ListView listView;
//    DrawerLayout drawerLayout;
//    ImageView openDrawer;
//    ActionBarDrawerToggle actionBarDrawerToggle;
//    int AUTOCOMPLETE_SOURCE = 1, AUTOCOMPLETE_DESTINATITON = 2;
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_user_module);
//        listView = findViewById(R.id.left_drawer);
//        openDrawer = findViewById(R.id.openDrawer);
//        drawerLayout = findViewById(R.id.drawerlayut);
//
//        openDrawer.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                // If navigation drawer is not open yet, open it else close it.
//                drawerLayout.addDrawerListener(actionBarDrawerToggle);
//                if (!drawerLayout.isDrawerOpen(GravityCompat.START))
//                    drawerLayout.openDrawer(Gravity.LEFT);
//                else drawerLayout.closeDrawer(Gravity.LEFT);
//            }
//        });
//
//        DrawerModel[] drawerItem = new DrawerModel[6];
//        drawerItem[0] = new DrawerModel(R.drawable.taxi, "Book Your Ride");
//        drawerItem[1] = new DrawerModel(R.drawable.your_ride, "Your Ride");
//        drawerItem[2] = new DrawerModel(R.drawable.rate_card, "Rate Card");
//        drawerItem[3] = new DrawerModel(R.drawable.support, "Support");
//        drawerItem[4] = new DrawerModel(R.drawable.about, "About");
//        drawerItem[5] = new DrawerModel(R.drawable.logout, "Logout");
//
//        DrawerI_Adapter adapter = new DrawerI_Adapter(this, R.layout.drawer_list_view, drawerItem);
//        listView.setOnItemClickListener(new DrawerItemClickListener());
//        listView.setAdapter(adapter);
//        selectItem(0);
//    }
//
//    @Override
//    public void picUpLocation() {
//
//        try {
////                    Intent intent =
////                            new PlaceAutocomplete.IntentBuilder(PlaceAutocomplete.MODE_OVERLAY).build(activity);
////                    startActivityForResult(intent, AUTOCOMPLETE_SOURCE);
//            PlacePicker.IntentBuilder builder = new PlacePicker.IntentBuilder();
//            startActivityForResult(builder.build(this), AUTOCOMPLETE_SOURCE);
//        } catch (GooglePlayServicesRepairableException e) {
//            // TODO: Handle the error.
////                    Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
//        } catch (GooglePlayServicesNotAvailableException e) {
//            // TODO: Handle the error.
////                    Toast.makeText(getApplicationContext(), e.getMessage().toString(), Toast.LENGTH_LONG).show();
//        }
//    }
//
//    private class DrawerItemClickListener implements AdapterView.OnItemClickListener {
//        @Override
//        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
//            selectItem(position);
//        }
//    }
//
//    private void selectItem(int position) {
//        Fragment fragment = null;
//        switch (position) {
//            case 0:
//                fragment = new BookRide();
//                drawerLayout.closeDrawers();
//                break;
//            case 1:
//                fragment = new Your_Rides();
//                drawerLayout.closeDrawers();
//                break;
//            case 2:
//                fragment = new RateCardFragment();
//                drawerLayout.closeDrawers();
//                break;
//            case 3:
//                fragment = new Support_Us();
//                drawerLayout.closeDrawers();
//                break;
//            case 4:
//                fragment = new AboutUs();
//                drawerLayout.closeDrawers();
//                break;
//            case 5:
//                // logout code here
//                showLogoutDialog();
//                drawerLayout.closeDrawers();
//                break;
//        }
//        if (fragment != null) {
//            FragmentManager fragmentManager = getSupportFragmentManager();
//            fragmentManager.beginTransaction().replace(R.id.container, fragment).commit();
//            listView.setItemChecked(position, true);
//            listView.setSelection(position);
//        } else {
//            Log.e("MainActivity", "Error in creating fragment");
//        }
//    }
//
//    public void showLogoutDialog() {
//        AlertDialog.Builder alertDialog = new AlertDialog.Builder(this);
//
//        //Setting Dialog Title
//        alertDialog.setTitle("Warning");
//
//        //Setting Dialog Message
//        alertDialog.setMessage("Are You sure ?");
//
//        //On Pressing Setting button
//        alertDialog.setPositiveButton("Logout", new DialogInterface.OnClickListener() {
//            @Override
//            public void onClick(DialogInterface dialog, int which) {
//                MySharedPrefrence sharedPrefrence = MySharedPrefrence.instanceOf(getApplicationContext());
//                sharedPrefrence.setLoggedIn(false);
//                Intent intent = new Intent(UserModuleActivity.this, Countinue_As_Acrtivity.class);
//                startActivity(intent);
//                finish();
//            }
//        });
//
//        //On pressing cancel button
//        alertDialog.setNegativeButton(R.string.cancel, new DialogInterface.OnClickListener() {
//            @Override
//            public void onClick(DialogInterface dialog, int which) {
//                dialog.cancel();
//            }
//        });
//        alertDialog.show();
//    }
//
//    @Override
//    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
//        super.onActivityResult(requestCode, resultCode, data);
//        if (requestCode == AUTOCOMPLETE_SOURCE) {
//            if (resultCode == RESULT_OK) {
//                Place place = PlacePicker.getPlace(this, data);
//                Log.i(TAG, "Place: " + place.getName());
//                source_location.setText(place.getName());
//
//                if (source_location_marker != null) {
//                    source_location_marker.remove();
//                }
//
//                LatLng latLng = place.getLatLng();
//                MarkerOptions markerOptions = new MarkerOptions();
//                markerOptions.position(latLng);
//                markerOptions.title("Source");
//
//                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.marker_new);
//                Bitmap b = bitmapDrawable.getBitmap();
//                Bitmap smallCar = Bitmap.createScaledBitmap(b, 150, 81, false);
//
//                markerOptions.icon(BitmapDescriptorFactory.fromBitmap(smallCar));
////                markerOptions.rotation(location.getBearing());
//                source_location_marker = mMap.addMarker(markerOptions);
//
//                mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(source_location_marker.getPosition(),15.0f));
//                setNearbyCabsOnMap(latLng);
//
//
//            } else if (resultCode == PlaceAutocomplete.RESULT_ERROR) {
//                Status status = PlaceAutocomplete.getStatus(this, data);
//                // TODO: Handle the error.
//                Log.i(TAG, status.getStatusMessage());
//
//            } else if (resultCode == RESULT_CANCELED) {
//                // The user canceled the operation.
//            }
//        } else if (requestCode == AUTOCOMPLETE_DESTINATITON) {
//            if (resultCode == RESULT_OK && data !=null) {
////                Place place = PlaceAutocomplete.getPlace(this, data);
//                //  Place place = PlacePicker.getPlace(this, data);
//                // Log.i(TAG, "Place: " + place.getName());
//
//
//                String[] datas= data.getStringArrayExtra("result");
//                destination_location.setText(datas[0]);
//
//                if (destination_location_marker != null) {
//                    destination_location_marker.remove();
//                }
//
//
//                LatLng latLng = new LatLng(Double.parseDouble(datas[1]), Double.parseDouble(datas[2]));
//                MarkerOptions markerOptions = new MarkerOptions();
//                markerOptions.position(latLng);
//                markerOptions.title("Destination");
//                BitmapDrawable bitmapDrawable = (BitmapDrawable) getResources().getDrawable(R.drawable.destination_marker);
//                Bitmap b = bitmapDrawable.getBitmap();
//                Bitmap dest = Bitmap.createScaledBitmap(b, 150, 81, false);
//
//                markerOptions.icon(BitmapDescriptorFactory.fromBitmap(dest));
//                ///markerOptions.rotation(latLng.getBearing());
//                destination_location_marker = mMap.addMarker(markerOptions);
//
//
//                if (!source_location.getText().toString().equals("") && !destination_location.getText().toString().equals("")) {
//                    String url = getDirectionsUrl(source_location_marker.getPosition(), destination_location_marker.getPosition());
////                    DownloadTask downloadTask = new DownloadTask(false);
////
////                    // Start downloading json data from Google Directions API
////                    downloadTask.execute(url);
//
//                    btnBookNow.setVisibility(View.VISIBLE);
//                    btnBookNow_layout.setVisibility(View.VISIBLE);
//                } else {
//                    btnBookNow.setVisibility(View.GONE);
//                    btnBookNow_layout.setVisibility(View.GONE);
//                }
//
//            } else if (resultCode == PlaceAutocomplete.RESULT_ERROR) {
//                Status status = PlaceAutocomplete.getStatus(this, data);
//                // TODO: Handle the error.
//                Log.i(TAG, status.getStatusMessage());
//
//            } else if (resultCode == RESULT_CANCELED) {
//                // The user canceled the operation.
//            }
//        }
//    }
//
//
//}
