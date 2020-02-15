package com.MedAmbulance.Fragments;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import com.MedAmbulance.Activity.BookAmbulance;
import com.MedAmbulance.Activity.Current_Location_Activity;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.R;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONException;
import org.json.JSONObject;

public class Login_Fragment extends Fragment implements View.OnClickListener , MyResult {

    Button login;
    TextInputEditText mobile, pwd;
    TextInputLayout t_mobile,t_psswd;
    String  userType="";
    private ProgressDialog progressDialog;
    MySharedPrefrence m;
    MyResult myResult;

    public Login_Fragment(String userType)
    {
        this.userType=userType;
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View view=inflater.inflate(R.layout.fragment_login_, container, false);
        login=view.findViewById(R.id.login);
        mobile=view.findViewById(R.id.mobile);
        pwd=view.findViewById(R.id.password);
        t_mobile=view.findViewById(R.id.t_mobile);
        t_psswd=view.findViewById(R.id.t_password);
        this.myResult=this;
        login.setOnClickListener(this);
        return view;
    }

    @Override
    public void onClick(View v) {
        switch (v.getId())
        {
            case  R.id.login:
                if (!mobile.getText().toString().isEmpty() && !pwd.getText().toString().isEmpty()) {
                    progressDialog = new ProgressDialog(getContext());
                    progressDialog.setMessage("Loading...");
                    progressDialog.setCancelable(true);
                    progressDialog.show();
                    Api_Calling.postMethodCall(getContext(), URLS.LOGIN,v,myResult,"Login",loginJon());
                }else {
                    Utility.topSnakBar(getContext(),v, Constant.PLEASE_FILL_ALL_FIELD);

                }
                break;
        }

    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
        if(progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
           if(object!=null && status)
           {
            startActivity(new Intent(getContext(), BookAmbulance.class));
           }


        }
        public JSONObject loginJon()
        {
            JSONObject jsonObject=new JSONObject();
            try {
                jsonObject.put("mobile",""+mobile.getText().toString()).put("password",""+pwd.getText().toString());
            } catch (JSONException e) {
                e.printStackTrace();
            }
            return jsonObject;


        }

}