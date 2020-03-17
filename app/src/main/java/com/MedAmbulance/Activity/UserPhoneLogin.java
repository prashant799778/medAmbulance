package com.MedAmbulance.Activity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.os.Parcelable;
import android.text.Editable;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

import androidx.appcompat.app.AppCompatActivity;

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.R;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class UserPhoneLogin extends AppCompatActivity implements View.OnClickListener ,MyResult{

    LinearLayout linearLayout;
    Button buttonCont;

    TextInputEditText usermobile;
    MyResult myResult;
    MySharedPrefrence m;
    int userTypeID= 2;
    String MobilePattern = "[0-9]{10}";
    TextInputLayout u_mobile;

    ProgressDialog progressDialog;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_phone_login);
        Animatoo.animateFade(UserPhoneLogin.this);

        m=MySharedPrefrence.instanceOf(getApplicationContext());

        this.myResult=this;


        linearLayout=findViewById(R.id.agree_terms);
        buttonCont=findViewById(R.id.phone_continue);
        u_mobile = findViewById(R.id.user_mobile);
        usermobile=findViewById(R.id.user_mobile_edt);


        linearLayout.setOnClickListener(this);
        buttonCont.setOnClickListener(this);

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSwipeRight(UserPhoneLogin.this);


    }

    @Override
    public void onClick(View v) {

        switch (v.getId()){
            case R.id.agree_terms:
                Intent i=new Intent(UserPhoneLogin.this, TermsConditions.class);
                startActivity(i);
                break;

            case R.id.phone_continue:

                if (!usermobile.getText().toString().isEmpty()){

                    if (usermobile.getText().toString().matches(MobilePattern)) {

                        progressDialog = new ProgressDialog(UserPhoneLogin.this);
                        progressDialog.setMessage("Loading...");
                        progressDialog.setCancelable(true);
                        progressDialog.show();
                        Api_Calling.postMethodCall(UserPhoneLogin.this, URLS.USERSIGNUP, getWindow().getDecorView().getRootView(),myResult,"UserSignUp",UserSginUp());

                    }
                    else {
                        Utility.topSnakBar(UserPhoneLogin.this,v, Constant.MobileLength);
                    }
                }

                else {
                    Utility.topSnakBar(UserPhoneLogin.this,v, Constant.SOMETHING_WENT_WRONG);

                }

        }
    }

    private JSONObject UserSginUp() {

        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("mobileNo",""+usermobile.getText().toString())
                    .put("userTypeId",""+userTypeID);

        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

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
//                JSONArray jsonArray= null;
//                jsonArray = object.getJSONArray("result");
//                for(int j=0;j<jsonArray.length();j++){
//                    JSONObject jsonObject= jsonArray.getJSONObject(j);
//                    otp = jsonObject.getString("otp");
//                }
                JSONObject jsonObject= object.getJSONObject("result");
                otp = jsonObject.getString("otp");
// m.setMobile(Utility.getValueFromJsonObject(object, "mobileNo"));
// m.setUserId(Utility.getValueFromJsonObject(object,"userId"));
// m.setUserTypeId(Utility.getValueFromJsonObject(object,"usertypeId"));
// m.setcurrentLocation(Utility.getValueFromJsonObject(object,"currentLocation"));
// m.setcurrentLocationlatlong(Utility.getValueFromJsonObject(object,"currentLocation"));
// m.setotp(Utility.getValueFromJsonObject(object,"otp"));

                Intent verificationIntent = new Intent(UserPhoneLogin.this, Verification_Activity.class);
                verificationIntent.putExtra("otp", otp);
                verificationIntent.putExtra("mobile", usermobile.getText().toString());
                startActivity(verificationIntent);

            }
            catch (Exception e) {
                e.printStackTrace();
            }

        }

    }
}