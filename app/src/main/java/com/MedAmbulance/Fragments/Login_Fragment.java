package com.MedAmbulance.Fragments;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;

import androidx.fragment.app.Fragment;

import com.MedAmbulance.Activity.DriverMainActivity;
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
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONException;
import org.json.JSONObject;

public class Login_Fragment extends Fragment implements View.OnClickListener , MyResult {

    LinearLayout linearLayout;
    Button buttonCont;
    TextInputEditText usermobile;
    MyResult myResult;
    MySharedPrefrence m;
    String userType= null;
    String MobilePattern = "[0-9]{10}";
    TextInputLayout u_mobile;

    ProgressDialog progressDialog;

    public Login_Fragment(String userType)
    {
        this.userType=userType;
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View view=inflater.inflate(R.layout.fragment_login_, container, false);
        Animatoo.animateFade(getContext());
        m=MySharedPrefrence.instanceOf(getContext());

        this.myResult=this;

        linearLayout=view.findViewById(R.id.agree_terms);
        buttonCont=view.findViewById(R.id.phone_continue);
        u_mobile = view.findViewById(R.id.user_mobile);
        usermobile=view.findViewById(R.id.user_mobile_edt);


        linearLayout.setOnClickListener(this);
        buttonCont.setOnClickListener(this);

       /* login=view.findViewById(R.id.login);
        mobile=view.findViewById(R.id.mobile);
        pwd=view.findViewById(R.id.password);
        t_mobile=view.findViewById(R.id.t_mobile);
        t_psswd=view.findViewById(R.id.t_password);
        this.myResult=this;
        login.setOnClickListener(this);*/
        return view;
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.agree_terms:
                /*Intent i=new Intent(getContext(), TermsConditions.class);
                startActivity(i);*/
                break;

            case R.id.phone_continue:

                if (!usermobile.getText().toString().isEmpty()){

                    if (usermobile.getText().toString().matches(MobilePattern)) {

                        progressDialog = new ProgressDialog(getContext());
                        progressDialog.setMessage("Loading...");
                        progressDialog.setCancelable(true);
                        progressDialog.show();
                        Api_Calling.postMethodCall(getContext(), URLS.USERSIGNUP, getActivity().getWindow().getDecorView().getRootView(),myResult,"UserSignUp",UserSginUp());

                    }
                    else {
                        Utility.topSnakBar(getContext(),v, Constant.MobileLength);
                    }
                }

                else {
                    Utility.topSnakBar(getContext(),v, Constant.SOMETHING_WENT_WRONG);

                }

        }
       /* switch (v.getId())
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
        }*/

    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
       /* if(progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status)
        {
            startActivity(new Intent(getContext(), DriverMainActivity.class));
        }*/


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

                Intent verificationIntent = new Intent(getContext(), Verification_Activity.class);
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
