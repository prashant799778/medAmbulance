package com.MedAmbulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.icu.text.CaseMap;
import android.os.Bundle;
import android.text.Editable;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.Switch;

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Comman.Validation;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_regular_EditText;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONException;
import org.json.JSONObject;

public class UserPhoneLogin extends AppCompatActivity implements View.OnClickListener ,MyResult{

    LinearLayout linearLayout;
    Button buttonCont;

    TextInputEditText usermobile;
    MyResult myResult;
    int  userTypeID= 2;
    TextInputLayout u_mobile;
    ProgressDialog progressDialog;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_phone_login);
        Animatoo.animateFade(UserPhoneLogin.this);


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

            case  R.id.phone_continue:

                if (!usermobile.getText().toString().isEmpty()){
                    progressDialog = new ProgressDialog(UserPhoneLogin.this);
                    progressDialog.setMessage("Loading...");
                    progressDialog.setCancelable(true);
                    progressDialog.show();
                    Api_Calling.postMethodCall(UserPhoneLogin.this, URLS.USERSIGNUP, getWindow().getDecorView().getRootView(),myResult,"UserSignUp",UserSginUp());

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
        if(progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status)
        {
            startActivity(new Intent(UserPhoneLogin.this, Verification_Activity.class));
        }


    }
}
