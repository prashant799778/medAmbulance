package com.example.respondermedambulance.Activity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import com.blogspot.atifsoftwares.animatoolib.Animatoo;

import com.example.respondermedambulance.Api_Calling.MyResult;
import com.example.respondermedambulance.Comman.Api_Calling;
import com.example.respondermedambulance.Comman.URLS;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.Model.EndRideModel;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_Bold;
import com.example.respondermedambulance.Widget.Atami_Regular;
import com.whinc.widget.ratingbar.RatingBar;

import org.json.JSONException;
import org.json.JSONObject;

public class End_Ride_Activity extends AppCompatActivity implements MyResult {

    Atami_Bold userName;
    EndRideModel data;
    MyResult result;
    ImageView move_back;
    private float ratedValue;
    com.whinc.widget.ratingbar.RatingBar wratingBar;
    JSONObject jsonObject=new JSONObject();
    Atami_Regular tvRateMessage,start_Address,end_Address,distance,distance_from_customer,estimatePice,tvRateCount;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_end__ride_);
        Animatoo.animateSlideLeft(End_Ride_Activity.this);
        userName=findViewById(R.id.user_name);
        tvRateCount=findViewById(R.id.value);
        tvRateMessage=findViewById(R.id.date);
        wratingBar=findViewById(R.id.rating);
        this.result=this;
        move_back=findViewById(R.id.move_back);
        start_Address=findViewById(R.id.start_address);
        end_Address=findViewById(R.id.end_address);
        distance=findViewById(R.id.distance);
        distance_from_customer=findViewById(R.id.distance_from_customer);
        estimatePice=findViewById(R.id.estimatePrice);

        Intent intent=getIntent();
        if(intent!=null)
            data=(EndRideModel) intent.getSerializableExtra("data");
//        if (data.getStartTime()!=null)
//            date.setText(data.getStartTime());;
        if (data.getUserName()!=null)
            userName.setText(data.getUserName());
        if (data.getPickup()!=null)
            start_Address.setText(data.getPickup());
        if (data.getDropOff()!=null)
            end_Address.setText(data.getDropOff());
        if (data.getTotalDistance()!=null)
            distance.setText(data.getTotalDistance());
        if (data.getFinalAmount()!=null)
            estimatePice.setText(data.getFinalAmount());
        if (data.getAmbulanceNo()!=null)
            distance_from_customer.setText(data.getUserMobile());
        move_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });

        wratingBar.setOnRatingChangeListener(new com.whinc.widget.ratingbar.RatingBar.OnRatingChangeListener() {
            @Override
            public void onChange(RatingBar ratingBar, int i, int i1) {
                tvRateMessage.setText("Thank you..!!!");
                Api_Calling.postMethodCall(End_Ride_Activity.this, URLS.addDriverRating,getWindow().getDecorView().getRootView(),result,"",ratingJSon(i1));
            }
        });




//        ratingBar.setMax(5);
//        ratingBar.setStepSize(1);
//        ratingBar.setNumStars(5);
//        ratingBar.setIsIndicator(true);
//        ratingBar.setOnRatingBarChangeListener(new RatingBar.OnRatingBarChangeListener() {
//            @Override
//            public void onRatingChanged(RatingBar ratingBar, float rating, boolean fromUser) {
//                ratedValue = ratingBar.getRating();
//                Api_Calling.postMethodCall(End_Ride_Activity.this, URLS.addDriverRating,getWindow().getDecorView().getRootView(),result,"",ratingJSon());
//                tvRateCount.setText("Your Rating : "
//                        + ratedValue + "/5.");
//                if(ratedValue<1){
//
//                    tvRateMessage.setText("ohh ho...");
//
//                }else if(ratedValue<2){
//
//                    tvRateMessage.setText("Ok.");
//
//                }else if(ratedValue<3){
//
//                    tvRateMessage.setText("Not bad.");
//
//                }else if(ratedValue<4){
//
//                    tvRateMessage.setText("Nice");
//
//                }else if(ratedValue<5){
//
//                    tvRateMessage.setText("Very Nice");
//
//                }else if(ratedValue==5){
//
//                    tvRateMessage.setText("Thank you..!!!");
//                }
//            }
//        });
    }
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(End_Ride_Activity.this);
    }
    private JSONObject ratingJSon(int ratedValue)
    {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("userId",""+data.getDriverId()).put("bookingId",""+data.getBookingId()).put("ratingId",String.valueOf(ratedValue));
            Utility.log("RatingJSon",""+jsonObject.toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
        if(jsonObject!=null && status)
        {
        }
    }
}
