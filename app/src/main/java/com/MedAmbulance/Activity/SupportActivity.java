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

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Model.SupportAdapters;
import com.MedAmbulance.Model.SupportModel;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class SupportActivity extends AppCompatActivity implements MyResult {

    ImageView move_back;
    MyResult myResult;
    MySharedPrefrence m;
    ProgressDialog progressDialog;

    private RecyclerView mrecyclerView;
    private SupportAdapters supportAdapters;
    RelativeLayout relativeLayout;
    private ArrayList<SupportModel> MarrayList;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_support);
        this.myResult=this;
        m = MySharedPrefrence.instanceOf(SupportActivity.this);
        move_back = findViewById(R.id.move_back);
        move_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });

        relativeLayout=findViewById(R.id.no_data);
        progressDialog = new ProgressDialog(SupportActivity.this);
        progressDialog.setMessage(" Please wait ...");
        progressDialog.setCancelable(true);
        progressDialog.show();
        mrecyclerView=findViewById(R.id.support_view);

        mrecyclerView.setHasFixedSize(true);
        mrecyclerView.setLayoutManager(new LinearLayoutManager(SupportActivity.this));
        MarrayList= new ArrayList<>();
        supportAdapters=new SupportAdapters(SupportActivity.this,MarrayList);
        mrecyclerView.setAdapter(supportAdapters);
        Api_Calling.postMethodCall(SupportActivity.this, URLS.Support,getWindow().getDecorView().getRootView(),myResult,"Support",supportObject());


    }

    private JSONObject supportObject() {
        JSONObject jsonObject=new JSONObject();
        String userID="91dbe288564e11ea93d39ebd4d0189fc";
        try {
            jsonObject.put("userId",""+userID).put("userMobile",""+m.getMobile());
            Log.d("Support", "SupportObject: "+jsonObject);

        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
        Log.d("AG", "onResult: "+object);
        if (progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status){
            relativeLayout.setVisibility(View.GONE);

            Gson gson= new GsonBuilder().create();
            try {
                ArrayList<SupportModel> rm = gson.fromJson(object.getString("result"), new TypeToken<ArrayList<SupportModel>>(){}.getType());
                MarrayList.clear();
                MarrayList.addAll(rm);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            supportAdapters.notifyDataSetChanged();
        }

    }
}
