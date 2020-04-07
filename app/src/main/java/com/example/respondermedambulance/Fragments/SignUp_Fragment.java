package com.example.respondermedambulance.Fragments;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;

import com.example.respondermedambulance.Activity.Current_Location_Activity;
import com.example.respondermedambulance.Activity.Verification_Activity;
import com.example.respondermedambulance.Api_Calling.MyResult;
import com.example.respondermedambulance.Comman.Api_Calling;
import com.example.respondermedambulance.Comman.Constant;
import com.example.respondermedambulance.Comman.MySharedPrefrence;
import com.example.respondermedambulance.Comman.URLS;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.Comman.Validation;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_regular_EditText;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONException;
import org.json.JSONObject;


public class SignUp_Fragment extends Fragment implements MyResult {
    Button signUp;
    TextInputEditText mobile,userName,email,pwd,cnfirmPwd;
    String  userType="";
    TextInputLayout t_email;
    MyResult myResult;
    MySharedPrefrence m;
    private ProgressDialog progressDialog;

    public SignUp_Fragment(String userType)
    {
        this.userType=userType;
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view=inflater.inflate(R.layout.fragment_sign_up_, container, false);
        signUp=view.findViewById(R.id.signup);
        mobile=view.findViewById(R.id.mobile);
        userName=view.findViewById(R.id.username);
        email=view.findViewById(R.id.email);
        t_email=view.findViewById(R.id.t_email);
        pwd=view.findViewById(R.id.password);
        cnfirmPwd=view.findViewById(R.id.cnfirm);
        this.myResult=this;
        m=MySharedPrefrence.instanceOf(getContext());

        signUp.setOnClickListener(new View.OnClickListener() {


            @Override
            public void onClick(View v) {

                switch (v.getId())
                {
                    case  R.id.signup:
                        if (!mobile.getText().toString().isEmpty() && !pwd.getText().toString().isEmpty()
                                && !userName.getText().toString().isEmpty() && !email.getText().toString().isEmpty()
                                && !cnfirmPwd.getText().toString().isEmpty())

                            if (pwd.getText().toString().equals(cnfirmPwd.getText().toString()))

                            {
                                progressDialog = new ProgressDialog(getContext());
                                progressDialog.setMessage("Loading...");
                                progressDialog.setCancelable(true);
                                progressDialog.show();
                                Api_Calling.postMethodCall(getContext(), URLS.responderSignup,v,myResult,"SingUp",signUpJos());
                                break;
                            }else {
                                Utility.topSnakBar(getContext(),v, Constant.PASSWORD_NOT_MATCH);

                            }else {
                            Utility.topSnakBar(getContext(),v, Constant.PLEASE_FILL_ALL_FIELD);

                        }
                        break;
                }
            }
        });
        return view;
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
        if(progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status)
        {

            try {
                String otp = "";
//                }
                JSONObject jsonObject= object.getJSONObject("result");
                m.setMobile(Utility.getValueFromJsonObject(jsonObject, "mobileNo"));
                m.setUserId(Utility.getValueFromJsonObject(jsonObject,"userId"));
                m.setotp(Utility.getValueFromJsonObject(jsonObject,"otp"));
                Intent verificationIntent = new Intent(getContext(), Verification_Activity.class);
                startActivity(verificationIntent);

            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }
    public JSONObject signUpJos()
    {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("mobileNo",""+mobile.getText().toString()).put("password",""+pwd.getText().toString())
                    .put("name",""+userName.getText().toString()).put("email",""+email.getText().toString());
            Utility.log("SINGJSON",""+jsonObject.toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }
}