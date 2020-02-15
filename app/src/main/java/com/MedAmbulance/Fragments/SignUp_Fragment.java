package com.MedAmbulance.Fragments;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;

import com.MedAmbulance.Activity.Current_Location_Activity;
import com.MedAmbulance.Activity.Verification_Activity;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Comman.Validation;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_regular_EditText;
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
                            Api_Calling.postMethodCall(getContext(), URLS.ADD_USER,v,myResult,"SingUp",signUpJos());
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
            startActivity(new Intent(getContext(), Verification_Activity.class));
        }


    }
    public JSONObject signUpJos()
    {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("mobile",""+mobile.getText().toString()).put("password",""+pwd.getText().toString())
                    .put("name",""+userName.getText().toString()).put("email",""+email.getText().toString())
                    .put("userTypeId",""+userType);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }
}