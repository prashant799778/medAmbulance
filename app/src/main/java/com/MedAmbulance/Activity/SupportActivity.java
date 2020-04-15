package com.MedAmbulance.Activity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.RelativeLayout;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Adapters.MyTripAdapter;

import com.MedAmbulance.Adapters.YourRideAdpter;
import com.MedAmbulance.Adapters.YourRideAdpter1;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Model.SupportAdapters;
import com.MedAmbulance.Model.SupportModel;
import com.MedAmbulance.Model.YourRidesModel;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class SupportActivity extends AppCompatActivity implements MyResult {

    MyResult myResult;
    MySharedPrefrence m;
    ProgressDialog progressDialog;

    private RecyclerView mrecyclerView;
    private YourRideAdpter yourRideListAdapter;
    RelativeLayout relativeLayout;
    private ArrayList<YourRidesModel> YarrayList;


    private RecyclerView mrecyclerView1;
    private YourRideAdpter1 yourRideListAdapter1;
    ImageView move_back;
    private ArrayList<YourRidesModel> YarrayList1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_support);
        Animatoo.animateSlideLeft(SupportActivity.this);
        this.myResult=this;
        m = MySharedPrefrence.instanceOf(SupportActivity.this);
        this.myResult=this;
        relativeLayout=findViewById(R.id.no_data);
        move_back=findViewById(R.id.move_back);
        progressDialog = new ProgressDialog(SupportActivity.this);
        progressDialog.setMessage(" Please wait ...");
        progressDialog.setCancelable(true);
        progressDialog.show();
        mrecyclerView=findViewById(R.id.Your_Ride);
        mrecyclerView.setLayoutManager(new LinearLayoutManager(SupportActivity.this));

        mrecyclerView1=findViewById(R.id.Your_Ride1);
        mrecyclerView1.setLayoutManager(new LinearLayoutManager(SupportActivity.this));


        YarrayList= new ArrayList<>();
        yourRideListAdapter=new YourRideAdpter(SupportActivity.this,YarrayList);
        mrecyclerView.setAdapter(yourRideListAdapter);

     move_back.setOnClickListener(new View.OnClickListener() {
         @Override
         public void onClick(View v) {
             onBackPressed();
         }
     });

        YarrayList1= new ArrayList<>();
        yourRideListAdapter1=new YourRideAdpter1(SupportActivity.this,YarrayList1);
        mrecyclerView1.setAdapter(yourRideListAdapter1);
        Api_Calling.postMethodCall(SupportActivity.this, URLS.Support,getWindow().getDecorView().getRootView(),myResult,"Support",supportObject());
    }

    private JSONObject supportObject() {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("userId",""+m.getUserId()).put("userMobile",""+m.getMobile());
            Log.d("Support", "SupportObject: "+jsonObject);

        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(SupportActivity.this);
    }
    @Override
    public void onResult(JSONObject object, Boolean status) {
        Log.d("AGiiiiiiiiiiiiiiiiii", "onResult: "+object);
        if (progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status){
            relativeLayout.setVisibility(View.GONE);
            Gson gson= new GsonBuilder().create();
            try {
                if(object.getJSONObject("result").getJSONArray("ambulance").length()>0){
                    ArrayList<YourRidesModel> rm = gson.fromJson(object.getJSONObject("result").getString("ambulance"), new TypeToken<ArrayList<YourRidesModel>>(){}.getType());
                    YarrayList.clear();
                    YarrayList.addAll(rm);
                    Utility.log("ArraySize","---1--"+rm.size());
                    yourRideListAdapter.notifyDataSetChanged();}
                if(object.getJSONObject("result").getJSONArray("responder").length()>0){
                    ArrayList<YourRidesModel> rm1 = gson.fromJson(object.getJSONObject("result").getString("responder"), new TypeToken<ArrayList<YourRidesModel>>(){}.getType());
                    YarrayList1.clear();
                    YarrayList1.addAll(rm1);
                    Utility.log("ArraySize","---"+rm1.size());
                    yourRideListAdapter1.notifyDataSetChanged();
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }

        }

    }
}
