package com.example.drivermedambulance;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

import com.example.drivermedambulance.Activity.TermsConditions;
import com.example.drivermedambulance.Activity.Verification_Activity;
import com.example.drivermedambulance.Api_Calling.MyResult;
import com.example.drivermedambulance.Comman.Api_Calling;
import com.example.drivermedambulance.Comman.Constant;
import com.example.drivermedambulance.Comman.MySharedPrefrence;
import com.example.drivermedambulance.Comman.URLS;
import com.example.drivermedambulance.Comman.Utility;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONException;
import org.json.JSONObject;

public class DriverPhoneLogin extends AppCompatActivity implements MyResult, View.OnClickListener {

    LinearLayout linearLayout;
    Button buttonCont;
    TextInputEditText usermobile;
    MyResult myResult;
    MySharedPrefrence m;
    String userType= null;
    String MobilePattern = "[0-9]{10}";
    TextInputLayout u_mobile;

    ProgressDialog progressDialog;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver_phone_login);
        this.myResult=this;
        m=MySharedPrefrence.instanceOf(DriverPhoneLogin.this);
        linearLayout=findViewById(R.id.agree_terms);
        buttonCont=findViewById(R.id.phone_continue);
        u_mobile =findViewById(R.id.div_mobile);
        usermobile=findViewById(R.id.div_mobile_edt);


        linearLayout.setOnClickListener(this);
        buttonCont.setOnClickListener(this);

    }

    @Override
    public void onResult(JSONObject object, Boolean status) {

        if(progressDialog!=null && progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status)
        {

            Log.d("response", object.toString());
            try
            {
                String otp = "";
                JSONObject jsonObject= object.getJSONObject("result");
                otp = jsonObject.getString("otp");
                Intent verificationIntent = new Intent(DriverPhoneLogin.this, Verification_Activity.class);
                verificationIntent.putExtra("otp", otp);
                verificationIntent.putExtra("mobile", usermobile.getText().toString());
                verificationIntent.putExtra("isDriverLogin",true);
                startActivity(verificationIntent);
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.agree_terms:
                Intent i=new Intent(DriverPhoneLogin.this, TermsConditions.class);
                startActivity(i);
                break;

            case R.id.phone_continue:

                if (!usermobile.getText().toString().isEmpty()){

                    if (usermobile.getText().toString().matches(MobilePattern)) {

                        progressDialog = new ProgressDialog(DriverPhoneLogin.this);
                        progressDialog.setMessage("Loading...");
                        progressDialog.setCancelable(true);
                        progressDialog.show();
                        Api_Calling.postMethodCall(DriverPhoneLogin.this, URLS.USERSIGNUP,getWindow().getDecorView().getRootView(),myResult,"UserSignUp",UserSginUp());

                    }
                    else {
                        Utility.topSnakBar(DriverPhoneLogin.this,v, Constant.MobileLength);
                    }
                }

                else {
                    Utility.topSnakBar(DriverPhoneLogin.this,v, Constant.SOMETHING_WENT_WRONG);

                }

        }
    }

    private JSONObject UserSginUp() {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("mobileNo",""+usermobile.getText().toString())
                    .put("userTypeId","3");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;
    }
}
