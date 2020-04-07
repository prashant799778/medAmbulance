package com.example.respondermedambulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;

import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.example.respondermedambulance.Comman.MySharedPrefrence;
import com.example.respondermedambulance.R;

public class Driver_Registration extends AppCompatActivity implements View.OnClickListener {
    LinearLayout driverLicence,ambulanceRegistration,personalId;
    ImageView imageView1,imageView2,imageView3;
    MySharedPrefrence m;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver__registration);
        Animatoo.animateSlideLeft(Driver_Registration.this);
        m=MySharedPrefrence.instanceOf(Driver_Registration.this);
        driverLicence=findViewById(R.id.driverLicence);
        ambulanceRegistration=findViewById(R.id.ambulanceRegistration);
        personalId=findViewById(R.id.personalId);
        imageView1=findViewById(R.id.arrow1);
        imageView2=findViewById(R.id.arrow2);
        imageView3=findViewById(R.id.arrow3);
        imageView1.setBackgroundResource(R.drawable.move);
        imageView2.setBackgroundResource(R.drawable.move);
        imageView3.setBackgroundResource(R.drawable.move);
        driverLicence.setOnClickListener(this);
        ambulanceRegistration.setOnClickListener(this);
        personalId.setOnClickListener(this);
//        m.setLoggedIn(true);
    }
    @Override
    public void onClick(View v) {
        switch (v.getId())
        {
            case R.id.driverLicence:
                startActivity(new Intent(Driver_Registration.this,Driver_Licence_Activity.class));
                break;
            case R.id.ambulanceRegistration:
                startActivity(new Intent(Driver_Registration.this,Ambulance_Registration_Activity.class));
                break;
            case R.id.personalId:
                startActivity(new Intent(Driver_Registration.this,Driver_Personal_Activty.class));
                break;
        }
    }
}
