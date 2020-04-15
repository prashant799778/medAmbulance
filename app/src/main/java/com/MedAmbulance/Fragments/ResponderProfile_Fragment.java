package com.MedAmbulance.Fragments;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.fragment.app.Fragment;

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Api_Calling.OnSaveProfileResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Model.ProfileModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_regular_EditText;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;

public class ResponderProfile_Fragment extends Fragment implements MyResult, OnSaveProfileResult {

    MyResult myResult;
    OnSaveProfileResult onSaveResult;
    MySharedPrefrence m;
    Atami_regular_EditText name,mobile,email,password;
    ProgressDialog progressDialog;
    Button save;


    public ResponderProfile_Fragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {


        m = MySharedPrefrence.instanceOf(getContext());
         this.myResult=this;
         this.onSaveResult=this;
        progressDialog = new ProgressDialog(getContext());
        progressDialog.setMessage(" Please wait ...");
        progressDialog.setCancelable(true);
        progressDialog.show();
        Api_Calling.postMethodCall(getContext(), URLS.responderProfile,getActivity().getWindow().getDecorView().getRootView(),myResult,"userProfile",profileObject());
        View rootView = inflater.inflate(R.layout.responder_profile_fragment, container, false);

        name=rootView.findViewById(R.id.name_update);
        mobile=rootView.findViewById(R.id.mobile_update);
        email=rootView.findViewById(R.id.emai_update);
        password=rootView.findViewById(R.id.password_update);
        save=rootView.findViewById(R.id.update_user);
        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!mobile.getText().toString().isEmpty()){
                    progressDialog = new ProgressDialog(getContext());
                    progressDialog.setMessage("Updating Please wait ...");
                    progressDialog.setCancelable(true);
                    progressDialog.show();
                    Api_Calling.postMethodCall2(getContext(), URLS.updateresponderProfile,getActivity().getWindow().getDecorView().getRootView(),onSaveResult,"userUpdatedProfile",profileUpadateObject());

                }else
                    Utility.topSnakBar(getContext(),getActivity().getWindow().getDecorView().getRootView(), Constant.PLEASE_FILL_ALL_FIELD);


            }

            private JSONObject profileUpadateObject() {
                JSONObject jsonObject=new JSONObject();
                try {
                    jsonObject.put("userId",""+m.getUserId())
                              .put("mobileNo",""+mobile.getText().toString())
                              .put("name",""+name.getText().toString())
                              .put("email",""+email.getText().toString())
                              .put("password",""+password.getText().toString());
                    Log.d("profileUpdate", "profileObject: "+jsonObject);

                } catch (JSONException e) {
                    e.printStackTrace();
                }
                return jsonObject;
            }
        });
        return rootView;


    }

    private JSONObject profileObject(){

        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("userId",""+m.getUserId());
            Log.d("profile", "profileObject: "+jsonObject);

        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
        Utility.log("OnResult",""+object);

        if (progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if (object!=null && status) {
            Gson gson= new GsonBuilder().create();
            try {
                ProfileModel rm = gson.fromJson(object.getString("result"), new TypeToken<ProfileModel>() {
                }.getType());
                Utility.log("DATA", "" + rm.getMobileNo());
                name.setText(rm.getName());
                email.setText(rm.getEmail());
                mobile.setText(rm.getMobileNo());
                password.setText(rm.getPassword());
                m.setUserName(rm.getName());
                m.setMobile(rm.getMobileNo());
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }

    }
    @Override
    public void saveButtonResult(JSONObject object, Boolean status) {
        Utility.log("OnResultSave",""+object);
        if (progressDialog!=null && progressDialog.isShowing())
            progressDialog.dismiss();
        if (object!=null && status){
          //  Utility.topSnakBar(getContext(),view,"Your profile has been updated");
            m.setMobile(mobile.getText().toString());
            m.setUserName(name.getText().toString());
            Utility.topSnakBar(getContext(),getActivity().getWindow().getDecorView().getRootView(), Constant.upadate);

        }

    }
}
