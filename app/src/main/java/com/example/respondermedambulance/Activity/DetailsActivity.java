package com.example.respondermedambulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

import com.example.respondermedambulance.Model.myTripModel;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_Bold;
import com.example.respondermedambulance.Widget.Atami_Regular;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;

public class DetailsActivity extends AppCompatActivity {
    Atami_Bold userName;
    myTripModel data;
    ImageView move_back;
    Atami_Regular date,start_Address,end_Address,distance,distance_from_customer,estimatePice;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_details);
        Animatoo.animateSlideLeft(DetailsActivity.this);
        userName=findViewById(R.id.user_name);
        date=findViewById(R.id.date);
        move_back=findViewById(R.id.move_back);
        start_Address=findViewById(R.id.start_address);
        end_Address=findViewById(R.id.end_address);
        distance=findViewById(R.id.distance);
        distance_from_customer=findViewById(R.id.distance_from_customer);
        estimatePice=findViewById(R.id.estimatePrice);
        Intent intent=getIntent();
        if(intent!=null)
            data=(myTripModel)intent.getSerializableExtra("data");
        if (data.getStartTime()!=null)
        date.setText(data.getStartTime());
        if (data.getUserName()!=null)
        userName.setText(data.getUserName());
        if (data.getTripFrom()!=null)
        start_Address.setText(data.getTripFrom());
        if (data.getTripTo()!=null)
        end_Address.setText(data.getTripTo());
        if (data.getTotalDistance()!=null)
        distance.setText(data.getTotalDistance());
        if (data.getFinalAmount()!=null)
        estimatePice.setText(data.getFinalAmount());
        if (data.getDistancefromCustomer()!=null)
        distance_from_customer.setText(data.getDistancefromCustomer());
        move_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(DetailsActivity.this);
    }
}
