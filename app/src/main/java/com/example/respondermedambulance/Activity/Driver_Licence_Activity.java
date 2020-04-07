package com.example.respondermedambulance.Activity;

import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Rect;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.ImageView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.error.AuthFailureError;
import com.android.volley.error.VolleyError;
import com.android.volley.request.SimpleMultiPartRequest;
import com.android.volley.toolbox.Volley;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.bumptech.glide.Glide;

import com.example.respondermedambulance.Api_Calling.MyResult;
import com.example.respondermedambulance.Comman.Constant;
import com.example.respondermedambulance.Comman.MySharedPrefrence;
import com.example.respondermedambulance.Comman.URLS;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_Bold;
import com.example.respondermedambulance.Widget.Atami_Regular;
import com.example.respondermedambulance.Widget.Atami_regular_EditText;
import com.fxn.pix.Options;
import com.fxn.pix.Pix;
import com.google.android.material.card.MaterialCardView;
import com.google.android.material.dialog.MaterialAlertDialogBuilder;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;

public class Driver_Licence_Activity extends AppCompatActivity implements View.OnClickListener{
    ImageView upload_F, delete_F, image_F, upload_B, delete_B, image_B, bck;
    Button save;
    ImageView c1, c2;
    Atami_regular_EditText licenceNumber;
    ProgressDialog progressDialog;
    MaterialCardView cardView1, cardView2;
    ArrayList<String> frontArray;
    ArrayList<String> backtArray;
    Dialog dialog;
    MyResult myResult;
    String key ="1";
    MySharedPrefrence m;
    Bitmap bitmap1,bitmap2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver__licence_);
        Animatoo.animateSlideLeft(Driver_Licence_Activity.this);
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
//               if (frontArray==frontArray){
//                   Api_Calling.multiPartCall(Driver_Licence_Activity.this,getWindow().getDecorView().getRootView(),URLS.AddLicence,Upload(),myResult,"upload");
//
//               }else if (backtArray==backtArray){
//                   Api_Calling.multiPartCall1(Driver_Licence_Activity.this,getWindow().getDecorView().getRootView(),URLS.AddLicence,Upload(),myResult,"upload",backtArray);
//
//               }else {
//                   Toast.makeText(Driver_Licence_Activity.this,"Something wentwrong",Toast.LENGTH_SHORT);
//               }

                if(! licenceNumber.getText().toString().isEmpty() && frontArray.size()>0 && backtArray.size()>0) {
                    progressDialog = new ProgressDialog(Driver_Licence_Activity.this);
                    progressDialog.setMessage("Uploading, please wait...");
                    progressDialog.show();
                    upLoadImage();
                }else {
                    Utility.topSnakBar(Driver_Licence_Activity.this,getWindow().getDecorView().getRootView(), Constant.PLEASE_FILL_ALL_FIELD);
                }
                break;
            case R.id.bck:
                onBackPressed();
        }
    }

//    private void Upload() {
//        Utility.log("InsideMethod","InsideMethod");
//        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, URLS.AddLicence, new Response.Listener<NetworkResponse>() {
//            @Override
//            public void onResponse(NetworkResponse response) {
//                String resultResponse = new String(response.data);
//                try {
//                    JSONObject result = new JSONObject(resultResponse);
//                    String status = result.getString("status");
//                    String message = result.getString("message");
//                    if (status.equals(Constant.REQUEST_SUCCESS)) {
//                        // tell everybody you have succed upload image and post strings
//                        Log.i("Messsage", message);
//                    } else {
//                        Log.i("Unexpected", message);
//                    }
//                } catch (JSONException e) {
//                    e.printStackTrace();
//                }
//            }
//        }, new Response.ErrorListener() {
//            @Override
//            public void onErrorResponse(VolleyError error) {
//                NetworkResponse networkResponse = error.networkResponse;
//                String errorMessage = "Unknown error";
//                if (networkResponse == null) {
//                    if (error.getClass().equals(TimeoutError.class)) {
//                        errorMessage = "Request timeout";
//                    } else if (error.getClass().equals(NoConnectionError.class)) {
//                        errorMessage = "Failed to connect server";
//                    }
//                } else {
//                    String result = new String(networkResponse.data);
//                    try {
//                        JSONObject response = new JSONObject(result);
//                        String status = response.getString("status");
//                        String message = response.getString("message");
//
//                        Log.e("Error Status", status);
//                        Log.e("Error Message", message);
//
//                        if (networkResponse.statusCode == 404) {
//                            errorMessage = "Resource not found";
//                        } else if (networkResponse.statusCode == 401) {
//                            errorMessage = message+" Please login again";
//                        } else if (networkResponse.statusCode == 400) {
//                            errorMessage = message+ " Check your inputs";
//                        } else if (networkResponse.statusCode == 500) {
//                            errorMessage = message+" Something is getting wrong";
//                        }
//                    } catch (JSONException e) {
//                        e.printStackTrace();
//                    }
//                }
//                Log.i("Error", errorMessage);
//                error.printStackTrace();
//            }
//        }) {
//            @Override
//            protected Map<String, String> getParams() {
//                Map<String, String> params = new HashMap<>();
//                params.put("key",key);
//                params.put("DlNo", licenceNumber.getText().toString());
//                params.put("name", m.getname());
//                params.put("mobileNo", m.getMobile());
//                return params;
//            }
//
//            @Override
//            protected Map<String, DataPart> getByteData() {
//                Map<String, DataPart> params = new HashMap<>();
//                // file name could found file base or direct access from real path
//                // for now just get bitmap data from ImageView
//                params.put("DlFrontImage", new DataPart("file_avatar.jpg", AppHelper.getFileDataFromDrawable(getBaseContext(), image_F.getDrawable()), "image/jpeg"));
//                params.put("DlBackImage", new DataPart("file_cover.jpg", AppHelper.getFileDataFromDrawable(getBaseContext(), image_B.getDrawable()), "image/jpeg"));
//
//                return params;
//            }
//        };
//        RequestQueue requestQueue= Volley.newRequestQueue(Driver_Licence_Activity.this);
//        requestQueue.add(volleyMultipartRequest);
//
////        VolleySingleton.getInstance(getBaseContext()).addToRequestQueue(volleyMultipartRequest);
//    }
    private void upLoadImage()
    {
        SimpleMultiPartRequest simpleMultiPartRequest=new SimpleMultiPartRequest(Request.Method.POST, URLS.addResponder, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                Utility.log("Response",""+response);
                try {
                    JSONObject jsonObject=new JSONObject(response);
                    if(Boolean.parseBoolean(jsonObject.getString("status")))
                    {
                        if(!isFinishing()){
                            progressDialog.dismiss();
                            if(Boolean.parseBoolean(Utility.getValueFromJsonObject(jsonObject,"documentStatus")))
                            {
                                showPopup();
                            }else {
                                onBackPressed();
                            }
                        }
                    }else {
                        progressDialog.dismiss();
                        Utility.topSnakBar(Driver_Licence_Activity.this,getWindow().getDecorView().getRootView(),Utility.getValueFromJsonObject(jsonObject,"message"));
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                    progressDialog.dismiss();
                }
            }
        },new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Utility.log("ERROR",""+error.getMessage());
            }
        });
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("key",Integer.parseInt(key));
            jsonObject.put("DlNo", licenceNumber.getText().toString());
            jsonObject.put("name", m.getname());
            jsonObject.put("mobileNo", m.getMobile());
            jsonObject.put("driverTypeId",2);
            Utility.log("JSON",""+jsonObject);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        simpleMultiPartRequest.addStringParam("data",""+jsonObject.toString());
        if(frontArray!=null && frontArray.size()>0)
        simpleMultiPartRequest.addFile("DlFrontImage",""+new File(frontArray.get(0)));
        if(frontArray!=null && frontArray.size()>0)
            simpleMultiPartRequest.addFile("DlBackImage",""+new File(backtArray.get(0)));

        try {
            Utility.log("FinalData",""+simpleMultiPartRequest.getBody());
        } catch (AuthFailureError authFailureError) {
            authFailureError.printStackTrace();
        }
        RequestQueue requestQueue=Volley.newRequestQueue(Driver_Licence_Activity.this);
        requestQueue.add(simpleMultiPartRequest);
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
    private void showPopup()
    {
        Rect displayRectangle = new Rect();
        Window window = Driver_Licence_Activity.this.getWindow();
        window.getDecorView().getWindowVisibleDisplayFrame(displayRectangle);
        final MaterialAlertDialogBuilder alertDialogBuilder=new MaterialAlertDialogBuilder(Driver_Licence_Activity.this,R.style.custom_dialog);
        final AlertDialog alertDialog = alertDialogBuilder.create();
        alertDialogBuilder.setMessage(getResources().getString(R.string.verifiedText));
        final View dialogView = LayoutInflater.from(Driver_Licence_Activity.this).inflate(R.layout.custom_dialog, null, false);
        Button ok=dialogView.findViewById(R.id.buttonOk);
        Atami_Regular t2=dialogView.findViewById(R.id.t2);
        Atami_Bold t1=dialogView.findViewById(R.id.t1);
        t1.setText("Done");
        t2.setText(getResources().getString(R.string.doneText));
        ok.setText("Ok");
        alertDialog.setView(dialogView);
        alertDialog.show();
        alertDialog.setCancelable(false);
        ok.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                alertDialog.dismiss();
                startActivity(new Intent(Driver_Licence_Activity.this,ResponderMapsActivity.class));
                finish();
            }
        });
    }
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(Driver_Licence_Activity.this);
    }

}
