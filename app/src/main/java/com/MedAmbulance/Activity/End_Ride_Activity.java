package com.MedAmbulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Model.EndRideModel;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.whinc.widget.ratingbar.RatingBar;

import org.json.JSONException;
import org.json.JSONObject;



public class End_Ride_Activity extends AppCompatActivity implements MyResult {
    Atami_Bold userName;
    EndRideModel data;
    ImageView move_back;
    MyResult result;
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
        if (data.getDriverName()!=null)
            userName.setText(data.getDriverName());
        if (data.getPickup()!=null)
            start_Address.setText(data.getPickup());
        if (data.getDropOff()!=null)
            end_Address.setText(data.getDropOff());
        if (data.getTotalDistance()!=null)
            distance.setText(data.getTotalDistance());
        if (data.getFinalAmount()!=null)
            estimatePice.setText(data.getFinalAmount());
        if (data.getAmbulanceNo()!=null)
            distance_from_customer.setText(data.getAmbulanceNo());
        move_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });

//        com.whinc.widget.ratingbar.RatingBar ratingBar2 = new com.whinc.widget.ratingbar.RatingBar(this);
//        ratingBar2.setMaxCount(7);
//        ratingBar2.setCount(4);
//        ratingBar2.setFillDrawableRes(R.drawable.empty);
//        ratingBar2.setEmptyDrawableRes(R.drawable.fill);
//        ratingBar2.setSpace(0);
//        ratingBar2.setTouchRating(true);
//        ratingBar2.setClickRating(true);
//        ratingBar2.setOnRatingChangeListener(new com.whinc.widget.ratingbar.RatingBar.OnRatingChangeListener() {
//            @Override
//            public void onChange(com.whinc.widget.ratingbar.RatingBar ratingBar, int i, int i1) {
//                Log.i("TAG", String.format("previous count:%d, current count:%d", i, i1));
//                Toast.makeText(End_Ride_Activity.this, "kfdsdytyuoip[", Toast.LENGTH_SHORT).show();
//            }
//        });

        wratingBar.setOnRatingChangeListener(new RatingBar.OnRatingChangeListener() {
            @Override
            public void onChange(RatingBar ratingBar, int i, int i1) {
                tvRateMessage.setText("Thank you..!!!");
                Api_Calling.postMethodCall(End_Ride_Activity.this, URLS.addUserRating,getWindow().getDecorView().getRootView(),result,"",ratingJSon(i1));
            }
        });









//        ratingBar.setOnRatingBarChangeListener(new RatingBar.OnRatingBarChangeListener() {
//            @Override
//            public void onRatingChanged(RatingBar ratingBar, float rating, boolean fromUser) {
//                ratedValue = ratingBar.getRating();
//                Utility.log("ddddddd","AAAAAAAAAAAAAAAAAAAAAAA");
////                Api_Calling.postMethodCall(End_Ride_Activity.this, URLS.addUserRating,getWindow().getDecorView().getRootView(),result,"",ratingJSon());
//                tvRateCount.setText("Your Rating : "
//
//                        + ratedValue + "/5.");
//
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
//
//                }
//
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
            jsonObject.put("driverId",""+data.getDriverId()).put("bookingId",""+data.getBookingId()).put("ratingId",String.valueOf(ratedValue));
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
