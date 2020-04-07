package com.example.respondermedambulance.Fragments;

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

import com.example.respondermedambulance.Activity.DriverMainActivity;
import com.example.respondermedambulance.Activity.ResponderMapsActivity;
import com.example.respondermedambulance.Activity.TermsConditions;
import com.example.respondermedambulance.Activity.UserPhoneLogin;
import com.example.respondermedambulance.Activity.Verification_Activity;
import com.example.respondermedambulance.Api_Calling.MyResult;
import com.example.respondermedambulance.Comman.Api_Calling;
import com.example.respondermedambulance.Comman.Constant;
import com.example.respondermedambulance.Comman.MySharedPrefrence;
import com.example.respondermedambulance.Comman.URLS;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.R;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import org.json.JSONException;
import org.json.JSONObject;

public class Login_Fragment extends Fragment implements View.OnClickListener , MyResult {

    LinearLayout linearLayout;
    Button buttonCont;
    TextInputEditText usermobile,password;
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
        m=MySharedPrefrence.instanceOf(getContext());

        this.myResult=this;

        linearLayout=view.findViewById(R.id.agree_terms);
        buttonCont=view.findViewById(R.id.phone_continue);
        u_mobile = view.findViewById(R.id.user_mobile);
        usermobile=view.findViewById(R.id.user_mobile_edt);
        password=view.findViewById(R.id.password);


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

                if (!usermobile.getText().toString().isEmpty() && !password.getText().toString().isEmpty()){
                    if (usermobile.getText().toString().matches(MobilePattern)) {
                        progressDialog = new ProgressDialog(getContext());
                        progressDialog.setMessage("Loading...");
                        progressDialog.setCancelable(true);
                        progressDialog.show();
                        Api_Calling.postMethodCall(getContext(), URLS.responderLogin, getActivity().getWindow().getDecorView().getRootView(),myResult,"UserSignUp",UserSginUp());
                    }
                    else {
                        Utility.topSnakBar(getContext(),v, Constant.MobileLength);
                    }
                }else {
                    Utility.topSnakBar(getContext(),v, Constant.PLEASE_FILL_ALL_FIELD);
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
                JSONObject jsonObject= object.getJSONObject("result");
                if(jsonObject.getString("status").equalsIgnoreCase("1")){
                    m.setMobile(Utility.getValueFromJsonObject(jsonObject, "mobileNo"));
                    m.setUserId(Utility.getValueFromJsonObject(jsonObject,"userId"));
                    m.setUserName(Utility.getValueFromJsonObject(jsonObject,"name"));
                    m.setUserTypeId(Utility.getValueFromJsonObject(jsonObject,"usertypeId"));
                    m.setUserProfile(Utility.getValueFromJsonObject(jsonObject,"profilePic"));
                    Intent verificationIntent = new Intent(getContext(), ResponderMapsActivity.class);
                    startActivity(verificationIntent);
                    getActivity().finish();}else {
                    m.setMobile(Utility.getValueFromJsonObject(jsonObject, "mobileNo"));
                    m.setUserId(Utility.getValueFromJsonObject(jsonObject,"userId"));
                    m.setUserName(Utility.getValueFromJsonObject(jsonObject,"name"));
                    m.setUserTypeId(Utility.getValueFromJsonObject(jsonObject,"usertypeId"));
                    m.setUserProfile(Utility.getValueFromJsonObject(jsonObject,"profilePic"));
                    Intent verificationIntent = new Intent(getContext(), ResponderMapsActivity.class);
                    startActivity(verificationIntent);
                    getActivity().finish();
                }

            }
            catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    private JSONObject UserSginUp() {

        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("mobileNo",""+usermobile.getText().toString()).put("password",""+password.getText().toString());
            Utility.log("LoginJSon",""+jsonObject.toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }

}
