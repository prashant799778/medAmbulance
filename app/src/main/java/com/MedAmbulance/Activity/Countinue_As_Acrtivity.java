package com.MedAmbulance.Activity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import com.MedAmbulance.DriverPhoneLogin;
import com.MedAmbulance.R;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.card.MaterialCardView;

public class Countinue_As_Acrtivity extends AppCompatActivity implements View.OnClickListener {
    MaterialCardView user,responsder,driver;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_countinue__as__acrtivity);
        Animatoo.animateSlideLeft(Countinue_As_Acrtivity.this);
        user=findViewById(R.id.user);
        driver=findViewById(R.id.driver);
        responsder=findViewById(R.id.responsder);
        responsder.setOnClickListener(this);
        user.setOnClickListener(this);
        driver.setOnClickListener(this);
    }
    @Override
    public void onClick(View v) {
       switch (v
       .getId()){
           case R.id.responsder:
              Intent i=new Intent(Countinue_As_Acrtivity.this, UserPhoneLogin.class);
              i.putExtra("userType","4");
              startActivity(i);
              finish();
               break;
           case  R.id.user:
               Intent i1=new Intent(Countinue_As_Acrtivity.this, UserPhoneLogin.class);
               i1.putExtra("userType","2");
               startActivity(i1);
               finish();
               break;
           case R.id.driver:
               Intent i2=new Intent(Countinue_As_Acrtivity.this, UserPhoneLogin.class);
               i2.putExtra("userType","3");
               startActivity(i2);
               finish();
               break;
       }

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(Countinue_As_Acrtivity.this);
    }
}
