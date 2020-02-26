package com.MedAmbulance.Activity;

import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Constant;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_regular_EditText;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.error.NoConnectionError;
import com.android.volley.error.TimeoutError;
import com.android.volley.error.VolleyError;
import com.bumptech.glide.Glide;
import com.fxn.pix.Options;
import com.fxn.pix.Pix;
import com.google.android.material.card.MaterialCardView;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Driver_Licence_Activity extends AppCompatActivity implements View.OnClickListener{
    ImageView upload_F, delete_F, image_F, upload_B, delete_B, image_B, bck;
    Button save;
    ImageView c1, c2;
    Atami_regular_EditText licenceNumber;
    ProgressDialog progressDialog;
    MaterialCardView cardView1, cardView2;
    ArrayList<String> frontArray;
    ArrayList<String> backtArray;
    MySharedPrefrence m;
    Dialog dialog;
    MyResult myResult;
    String key ="1";
    Bitmap bitmap1,bitmap2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver__licence_);
        frontArray = new ArrayList<>();
        backtArray = new ArrayList<>();


        m = MySharedPrefrence.instanceOf(Driver_Licence_Activity.this);


        upload_F = findViewById(R.id.upload_F);
        upload_B = findViewById(R.id.upload_B);
        delete_F = findViewById(R.id.delete_F);
        delete_B = findViewById(R.id.delete_B);
        cardView1 = findViewById(R.id.card_1);
        cardView2 = findViewById(R.id.card_2);
        image_F = findViewById(R.id.f_image);
        image_B = findViewById(R.id.B_image);
        save = findViewById(R.id.save);
        bck = findViewById(R.id.bck);
        licenceNumber = findViewById(R.id.driverLicence);
        c1 = findViewById(R.id.camera1);
        c2 = findViewById(R.id.camera2);
        upload_F.setOnClickListener(this);
        upload_B.setOnClickListener(this);
        delete_B.setOnClickListener(this);
        delete_F.setOnClickListener(this);
        image_F.setOnClickListener(this);
        image_B.setOnClickListener(this);
        save.setOnClickListener(this);
        bck.setOnClickListener(this);
        cardView1.setOnClickListener(this);
        cardView2.setOnClickListener(this);
    }

    @Override
    protected void onStart() {
        super.onStart();
        if (frontArray.size() > 0) {
            c1.setVisibility(View.GONE);
        }
        if (backtArray.size() > 0) {
            c2.setVisibility(View.GONE);
        }
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.upload_F:
                Pix.start(Driver_Licence_Activity.this, Options.init().setRequestCode(100).setCount(1));
                break;
            case R.id.card_1:
                Pix.start(Driver_Licence_Activity.this, Options.init().setRequestCode(100).setCount(1));
                break;
            case R.id.delete_F:
                image_F.setVisibility(View.GONE);
                c1.setVisibility(View.VISIBLE);
                frontArray.clear();
                break;
            case R.id.upload_B:
                Pix.start(Driver_Licence_Activity.this, Options.init().setRequestCode(101).setCount(1));
                break;
            case R.id.card_2:
                Pix.start(Driver_Licence_Activity.this, Options.init().setRequestCode(101).setCount(1));
                break;
            case R.id.delete_B:
                image_B.setVisibility(View.GONE);
                c2.setVisibility(View.VISIBLE);
                backtArray.clear();
                break;
            case R.id.save:
             //  if (frontArray==frontArray){
                   //Api_Calling.multiPartCall(Driver_Licence_Activity.this,getWindow().getDecorView().getRootView(),URLS.AddLicence,Upload(),myResult,"upload");

             //  }else if (backtArray==backtArray){
              //     Api_Calling.multiPartCall1(Driver_Licence_Activity.this,getWindow().getDecorView().getRootView(),URLS.AddLicence,Upload(),myResult,"upload",backtArray);

//               }else {
//                   Toast.makeText(Driver_Licence_Activity.this,"Something wentwrong",Toast.LENGTH_SHORT);
//               }

                progressDialog = new ProgressDialog(Driver_Licence_Activity.this);
                progressDialog.setMessage("Uploading, please wait...");
                progressDialog.show();

                Upload();

                break;
            case R.id.bck:
                onBackPressed();
        }
    }

    private void Upload() {


        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, URLS.AddLicence, new Response.Listener<NetworkResponse>() {
            @Override
            public void onResponse(NetworkResponse response) {
                String resultResponse = new String(response.data);
                try {
                    JSONObject result = new JSONObject(resultResponse);
                    String status = result.getString("status");
                    String message = result.getString("message");

                    if (status.equals(Constant.REQUEST_SUCCESS)) {
                        // tell everybody you have succed upload image and post strings
                        Log.i("Messsage", message);
                    } else {
                        Log.i("Unexpected", message);
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                NetworkResponse networkResponse = error.networkResponse;
                String errorMessage = "Unknown error";
                if (networkResponse == null) {
                    if (error.getClass().equals(TimeoutError.class)) {
                        errorMessage = "Request timeout";
                    } else if (error.getClass().equals(NoConnectionError.class)) {
                        errorMessage = "Failed to connect server";
                    }
                } else {
                    String result = new String(networkResponse.data);
                    try {
                        JSONObject response = new JSONObject(result);
                        String status = response.getString("status");
                        String message = response.getString("message");

                        Log.e("Error Status", status);
                        Log.e("Error Message", message);

                        if (networkResponse.statusCode == 404) {
                            errorMessage = "Resource not found";
                        } else if (networkResponse.statusCode == 401) {
                            errorMessage = message+" Please login again";
                        } else if (networkResponse.statusCode == 400) {
                            errorMessage = message+ " Check your inputs";
                        } else if (networkResponse.statusCode == 500) {
                            errorMessage = message+" Something is getting wrong";
                        }
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                Log.i("Error", errorMessage);
                error.printStackTrace();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("key",key);
                params.put("DlNo", licenceNumber.getText().toString());
                params.put("name", m.getname());
                params.put("mobileNo", m.getMobile());
                return params;
            }

            @Override
            protected Map<String, DataPart> getByteData() {
                Map<String, DataPart> params = new HashMap<>();
                // file name could found file base or direct access from real path
                // for now just get bitmap data from ImageView
                params.put("DlFrontImage", new DataPart("file_avatar.jpg", AppHelper.getFileDataFromDrawable(getBaseContext(), image_F.getDrawable()), "image/jpeg"));
                params.put("DlBackImage", new DataPart("file_cover.jpg", AppHelper.getFileDataFromDrawable(getBaseContext(), image_B.getDrawable()), "image/jpeg"));

                return params;
            }
        };

       // VolleySingleton.getInstance(getBaseContext()).addToRequestQueue(volleyMultipartRequest);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == Activity.RESULT_OK && requestCode == 100) {
            if(data!=null)
                frontArray = data.getStringArrayListExtra(Pix.IMAGE_RESULTS);
            if(frontArray.size()>0 && frontArray !=null){
                Glide.with(Driver_Licence_Activity.this).load(frontArray.get(0)).into(image_F);
                image_F.setVisibility(View.VISIBLE);
                // bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(),);

            }
        }else {
            if(data!=null){
                backtArray = data.getStringArrayListExtra(Pix.IMAGE_RESULTS);
                if(backtArray.size()>0 && backtArray !=null){
                    Glide.with(Driver_Licence_Activity.this).load(backtArray.get(0)).into(image_B);
                    image_B.setVisibility(View.VISIBLE);
                }
            }}
    }



}
