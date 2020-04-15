package com.MedAmbulance.Activity;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Rect;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.widget.Button;

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Regular;
import com.MedAmbulance.Widget.OtpEditText;
import com.MedAmbulance.util.AppUtil;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.dialog.MaterialAlertDialogBuilder;

import org.json.JSONException;
import org.json.JSONObject;

public class Verification_Activity extends AppCompatActivity implements MyResult {
    OtpEditText otpEditText,userMobile;
    Button done;
    Context context;
    Atami_Regular  info_text,don_not_otp;
    MyResult myResult;

    MySharedPrefrence m;
    String mobile;
    private ProgressDialog progressDialog;
    private boolean isDriverLogin = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_verification_);
        Animatoo.animateSlideLeft(Verification_Activity.this);
        isDriverLogin = getIntent().getBooleanExtra("isDriverLogin",false);
        //otpEditText
        otpEditText=findViewById(R.id.et_otp);
        info_text=findViewById(R.id.text);
        don_not_otp=findViewById(R.id.dontgetotp);

        this.myResult=this;
        m= MySharedPrefrence.instanceOf(getApplicationContext());

        //VerifyButton Click
        done=findViewById(R.id.done);
        mobile = getIntent().getStringExtra("mobile");
        don_not_otp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });


        info_text.setText(getResources().getString(R.string.verifyText)+" "+mobile);
        done.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
        // startActivity(new Intent(Verification_Activity.this,Driver_Registration.class));
                Rect displayRectangle = new Rect();
                Window window = Verification_Activity.this.getWindow();
                window.getDecorView().getWindowVisibleDisplayFrame(displayRectangle);
                final MaterialAlertDialogBuilder alertDialogBuilder=new MaterialAlertDialogBuilder(Verification_Activity.this,R.style.custom_dialog);
                final AlertDialog alertDialog = alertDialogBuilder.create();
                alertDialogBuilder.setMessage(getResources().getString(R.string.doneText));
                final View dialogView = LayoutInflater.from(v.getContext()).inflate(R.layout.custom_dialog, null, false);


//DialogBox Start Button Click
                Button ok=dialogView.findViewById(R.id.buttonOk);
                alertDialog.setView(dialogView);
                alertDialog.show();
                ok.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
// startActivity(new Intent(Verification_Activity.this,Driver_Registration.class));

                        if (!otpEditText.getText().toString().isEmpty() ) {
                            progressDialog = new ProgressDialog(Verification_Activity.this);
                            progressDialog.setMessage("Loading...");
                            progressDialog.setCancelable(true);
                            progressDialog.show();
                            Api_Calling.postMethodCall(Verification_Activity.this, URLS.VERIFY, getWindow().getDecorView().getRootView(),myResult,"UserSignUp",startmain());
                        }else {
                            Utility.topSnakBar(context,v, Constant.PLEASE_FILL_ALL_FIELD);

                        }

                        alertDialog.dismiss();
                    }


                });
            }
        });

        String otp = getIntent().getExtras().getString("otp");

        if(otp != "")
            otpEditText.setText(otp);



    }

    @Override
    public void onResult(JSONObject object, Boolean status) {

        if(progressDialog!=null && progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status) {
            AppUtil.LogMsg("asdhhhhhhhhhhh", object.toString());
            JSONObject result = null;
            try {
                result = object.getJSONObject("result");
//                m.setUserId(AppUtil.getDatafromJSonObject(result, "userId"));
//                if (!isDriverLogin) {
//                    m.setUserTypeId(AppUtil.getDatafromJSonObject(result, "userTypeId"));
//                } else {
//                    m.setUserTypeId(String.valueOf(3));
//                }
//                m.setMobile(AppUtil.getDatafromJSonObject(result, "mobileNo"));
//                m.setLoggedIn(true);
//                if (m.getUserTypeId().equalsIgnoreCase("2"))
//                    startActivity(new Intent(Verification_Activity.this, MapsActivity.class));
//                if (m.getUserTypeId().equalsIgnoreCase("3"))
//                startActivity(new Intent(Verification_Activity.this, DriversMapsActivity.class));

                Utility.log("TESTTTTTTTTTT","SUerIdType In Verficaion"+AppUtil.getDatafromJSonObject(result,"userTypeId"));
//                if(AppUtil.getDatafromJSonObject(result,"userTypeId").equalsIgnoreCase("2"))
//                {
                    startActivity(new Intent(Verification_Activity.this, MapsActivity.class));
                    finish();
//                }else if(AppUtil.getDatafromJSonObject(result,"userTypeId").equalsIgnoreCase("3")){
//                    startActivity(new Intent(Verification_Activity.this, DriversMapsActivity.class));
//                    finish();
//                }else if(AppUtil.getDatafromJSonObject(result,"userTypeId").equalsIgnoreCase("4")){
//                    startActivity(new Intent(Verification_Activity.this, ResponderMapsActivity.class));
//                    finish();
//                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
            m.setMobile(Utility.getValueFromJsonObject(result, "mobileNo"));
            m.setUserId(Utility.getValueFromJsonObject(result, "userId"));
        }
    }

    public JSONObject startmain()
    {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("otp",""+otpEditText.getText().toString()).put("mobileNo",mobile);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        Utility.log("Data",""+jsonObject);
        return jsonObject;


    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(Verification_Activity.this);
    }
}
