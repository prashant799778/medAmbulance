package com.MedAmbulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.R;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.card.MaterialCardView;

public class SplaceActivity extends AppCompatActivity {
    MySharedPrefrence m;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        m= MySharedPrefrence.instanceOf(getApplicationContext());
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                 if(m.isLoggedIn()){


                     if(m.getUserTypeId().equalsIgnoreCase("2")){
                         startActivity(new Intent(SplaceActivity.this,MapsActivity.class));
                         finish();
                     }else if(m.getUserTypeId().equalsIgnoreCase("3")){

                         startActivity(new Intent(SplaceActivity.this,DriversMapsActivity.class));
                         finish();

                     }else {
                         startActivity(new Intent(SplaceActivity.this,Countinue_As_Acrtivity.class));
                             finish();
                     }
                 }else{
                     startActivity(new Intent(SplaceActivity.this,Countinue_As_Acrtivity.class));
                      finish();
                 }

            }
        },3000);
    }
}
