package com.MedAmbulance.Fragments;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;

import com.MedAmbulance.Activity.BookAmbulance;
import com.MedAmbulance.Activity.Current_Location_Activity;
import com.MedAmbulance.Activity.TermsConditions;
import com.MedAmbulance.Activity.UserPhoneLogin;
import com.MedAmbulance.Activity.Verification_Activity;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.R;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Login_Fragment extends Fragment implements View.OnClickListener , MyResult {

    LinearLayout linearLayout;
    Button buttonCont;

    TextInputEditText usermobile;
    MyResult myResult;
    MySharedPrefrence m;
   String userTypeID= "3";
    String MobilePattern = "[0-9]{10}";
    TextInputLayout u_mobile;

    ProgressDialog progressDialog;


    public Login_Fragment(String userType)
    {
        this.userTypeID=userType;
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View view=inflater.inflate(R.layout.fragment_login_, container, false);
        buttonCont=view.findViewById(R.id.phone_continue);
        u_mobile = view.findViewById(R.id.user_mobile);
        usermobile=view.findViewById(R.id.user_mobile_edt);
        buttonCont.setOnClickListener(this);
        this.myResult=this;
       // login.setOnClickListener(this);
        return view;
    }

    @Override
    public void onClick(View v) {

        switch (v.getId()){
            case R.id.agree_terms:
                Intent i=new Intent(getActivity(), TermsConditions.class);
                startActivity(i);
                break;

            case R.id.phone_continue:

                if (!usermobile.getText().toString().isEmpty()){

                    if (usermobile.getText().toString().matches(MobilePattern)) {

                        progressDialog = new ProgressDialog(getActivity());
                        progressDialog.setMessage("Loading...");
                        progressDialog.setCancelable(true);
                        progressDialog.show();
                        Api_Calling.postMethodCall(getActivity(), URLS.USERSIGNUP, v,myResult,"UserSignUp",UserSginUp());

                    }
                    else {
                        Utility.topSnakBar(getActivity(),v, Constant.MobileLength);
                    }
                }

                else {
                    Utility.topSnakBar(getActivity(),v, Constant.SOMETHING_WENT_WRONG);

                }

        }



    }

    @Override
    public void onResult(JSONObject object, Boolean status) {

        if(progressDialog!=null && progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status)
        {


            try
            {
                String otp = "";
//                JSONArray jsonArray= null;
//                jsonArray = object.getJSONArray("result");
//                for(int j=0;j<jsonArray.length();j++){
//                    JSONObject jsonObject= jsonArray.getJSONObject(j);
//                    otp = jsonObject.getString("otp");
//                }


                otp = object.getJSONObject("result").getString("otp");
                Intent verificationIntent = new Intent(getActivity(), Verification_Activity.class);
                verificationIntent.putExtra("otp", otp);
                verificationIntent.putExtra("mobile", usermobile.getText().toString());
                startActivity(verificationIntent);

            }
            catch (Exception e) {
                e.printStackTrace();
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


}