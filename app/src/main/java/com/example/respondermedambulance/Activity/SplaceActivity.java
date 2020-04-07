package com.example.respondermedambulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;

import com.example.respondermedambulance.Comman.MySharedPrefrence;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.R;
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
                    Utility.log("TESTTTTTTTTTT","SUerIdType"+m.getUserTypeId());
                    startActivity(new Intent(SplaceActivity.this,ResponderMapsActivity.class));
                    finish();
                }else{
                    Utility.log("TESTTTTTTTTTT","SUerIdTypeLoginStatus false");
                    startActivity(new Intent(SplaceActivity.this,Login.class));
                    finish();
                }

            }
        },1000);
    }
}
