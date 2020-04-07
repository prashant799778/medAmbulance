package com.example.drivermedambulance.Fragments;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.example.drivermedambulance.Api_Calling.MyResult;
import com.example.drivermedambulance.Api_Calling.OnSaveProfileResult;
import com.example.drivermedambulance.Comman.Api_Calling;
import com.example.drivermedambulance.Comman.Constant;
import com.example.drivermedambulance.Comman.MySharedPrefrence;

import com.example.drivermedambulance.Comman.URLS;
import com.example.drivermedambulance.Comman.Utility;
import com.example.drivermedambulance.Model.DriverprofileModel;
import com.example.drivermedambulance.Model.ProfileModel;
import com.example.drivermedambulance.R;
import com.example.drivermedambulance.Widget.Atami_regular_EditText;
import com.fxn.pix.Options;
import com.fxn.pix.Pix;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

import de.hdodenhof.circleimageview.CircleImageView;

public class DriverProfile_Fragment extends Fragment implements MyResult, OnSaveProfileResult {


    MyResult myResult;
    OnSaveProfileResult onSaveProfileResult;
    MySharedPrefrence m;
    Atami_regular_EditText name, mobile, email, password;
    ProgressDialog progressDialog;
    Button save;

    CircleImageView profile_image;
    ArrayList<String> imageArray = new ArrayList<>();


    public DriverProfile_Fragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        m = MySharedPrefrence.instanceOf(getContext());
        this.myResult = this;
        this.onSaveProfileResult = this;
        progressDialog = new ProgressDialog(getContext());
        progressDialog.setMessage(" Please wait ...");
        progressDialog.setCancelable(true);
        progressDialog.show();
        View rootView = inflater.inflate(R.layout.driver_profile_fragment, container, false);
        name = rootView.findViewById(R.id.name_update_div);
        mobile = rootView.findViewById(R.id.mobile_update_div);
        email = rootView.findViewById(R.id.emai_update_div);
        password = rootView.findViewById(R.id.password_update_div);
        save = rootView.findViewById(R.id.update_div);
        Api_Calling.postMethodCall(getContext(), URLS.DriverProfile, getActivity().getWindow().getDecorView().getRootView(), myResult, "DriverUpdatedProfile", DivProfileObject());

        profile_image = rootView.findViewById(R.id.profile_image);profile_image.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Pix.start(getActivity(), Options.init().setRequestCode(500).setCount(1));
            }
        });

        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!name.getText().toString().isEmpty() && !email.getText().toString().isEmpty() && !password.getText().toString().isEmpty() && !mobile.getText().toString().isEmpty()) {
                    progressDialog = new ProgressDialog(getContext());
                    progressDialog.setMessage("Updating Please wait ...");
                    progressDialog.setCancelable(true);
                    progressDialog.show();
                    Api_Calling.multiPartCall(getContext(), getActivity().getWindow().getDecorView().getRootView(),URLS.updateDriverProfile111, profileUpadateObject(),onSaveProfileResult,"",imageArray);
                } else
                    Utility.topSnakBar(getContext(), getActivity().getWindow().getDecorView().getRootView(), Constant.PLEASE_FILL_ALL_FIELD);
            }
            private JSONObject profileUpadateObject() {
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject.put("userId", "" + m.getUserId())
                            .put("mobileNo", "" + mobile.getText().toString())
                            .put("name", "" + name.getText().toString())
                            .put("email", "" + email.getText().toString())
                            .put("password", "" + password.getText().toString());
                    Log.d("profileUpdate", "profileObject: " + jsonObject);

                } catch (JSONException e) {
                    e.printStackTrace();
                }
                return jsonObject;
            }
        });

        return rootView;
    }


    public void setImage(int requestCode, int resultCode, @Nullable Intent data) {
        Utility.log("OnActivityResult", "OnActivityResult__Fragment");
        if (resultCode == getActivity().RESULT_OK && requestCode == 500) {
            imageArray = data.getStringArrayListExtra(Pix.IMAGE_RESULTS);
            if (imageArray.size() > 0) {
                Utility.setRoundedImage(getContext(), profile_image, imageArray.get(0).trim());
            }
        }
    }




    private JSONObject DivProfileObject() {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("userId",""+m.getUserId());
            Log.d("Divprofile", "profileObject: "+jsonObject);

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
                DriverprofileModel rm = gson.fromJson(object.getString("result"), new TypeToken<DriverprofileModel>() {
                }.getType());
                Utility.log("DATA", "" + rm.getMobileNo());
                name.setText(rm.getName());
                email.setText(rm.getEmail());
                mobile.setText(rm.getMobileNo());
                password.setText(rm.getPassword());
                Utility.setRoundedImage(getContext(),profile_image,rm.getProfilePic());
                m.setUserProfile(rm.getProfilePic());
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
            m.setMobile(mobile.getText().toString());
            m.setUserName(name.getText().toString());
            Utility.topSnakBar(getContext(),getActivity().getWindow().getDecorView().getRootView(), Constant.upadate);

        }
    }
}
