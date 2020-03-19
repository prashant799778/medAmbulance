package com.MedAmbulance.Activity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.Html;
import android.view.View;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import com.MedAmbulance.Activity.ui.AboutUs;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Regular;
import com.google.gson.JsonArray;

import org.json.JSONException;
import org.json.JSONObject;

public class AboutActivity extends AppCompatActivity implements MyResult {

    ImageView move_back;
    MyResult myResult;
    Atami_Regular msg,msg2,msg3;
    ImageView bck;
    ProgressDialog progressDialog;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);
        this.myResult=this;
        progressDialog = new ProgressDialog(AboutActivity.this);
        progressDialog.setMessage("Loading...");
        progressDialog.setCancelable(true);
        progressDialog.show();
        msg=findViewById(R.id.mgs);
        msg2=findViewById(R.id.mgs2);
        msg3=findViewById(R.id.mgs3);

        move_back = findViewById(R.id.move_back);
        move_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });
        Api_Calling.postMethodCall(AboutActivity.this, URLS.AboutUs,getWindow().getDecorView().getRootView(),myResult,"AboutUS",null);

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
        Utility.log("All About Us",""+object.toString());
        if(progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status)
        {
            try {
                JSONObject jsonObject1=object.getJSONArray("result").getJSONObject(0);
                msg.setText(Html.fromHtml(Utility.getValueFromJsonObject(jsonObject1,"contactNo")));
                msg2.setText(Html.fromHtml(Utility.getValueFromJsonObject(jsonObject1,"dateCreate")));
                msg3.setText(Html.fromHtml(Utility.getValueFromJsonObject(jsonObject1,"description")));


            } catch (JSONException e) {
                e.printStackTrace();
            }
        }

    }
}
