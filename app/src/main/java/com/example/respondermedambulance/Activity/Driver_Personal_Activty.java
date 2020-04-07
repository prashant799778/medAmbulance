package com.example.respondermedambulance.Activity;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
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

import com.example.respondermedambulance.Comman.Constant;
import com.example.respondermedambulance.Comman.MySharedPrefrence;
import com.example.respondermedambulance.Comman.URLS;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_Bold;
import com.example.respondermedambulance.Widget.Atami_Regular;
import com.example.respondermedambulance.Widget.Atami_regular_EditText;
import com.example.respondermedambulance.Widget.Custom_Spinner;
import com.fxn.pix.Options;
import com.fxn.pix.Pix;
import com.google.android.material.card.MaterialCardView;
import com.google.android.material.dialog.MaterialAlertDialogBuilder;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;

public class Driver_Personal_Activty extends AppCompatActivity implements View.OnClickListener {
    ImageView upload_F,delete_F,image_F,upload_B,delete_B,image_B,bck;
    Button save;
    ImageView c1,c2;
    Atami_regular_EditText licenceNumber;
    ArrayList<String>frontArray;
    MaterialCardView cardView1,cardView2;
    ArrayList<String>backtArray;
    Custom_Spinner idType;
    ArrayList<String>idList;
    String key ="2";
    ProgressDialog progressDialog;
    MySharedPrefrence m;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver__personal__activty);
        Animatoo.animateSlideLeft(Driver_Personal_Activty.this);
        frontArray=new ArrayList<>();
        backtArray=new ArrayList<>();
        idList=new ArrayList<>();
        cardView1=findViewById(R.id.card_1);
        cardView2=findViewById(R.id.card_2);
        upload_F=findViewById(R.id.upload_F);
        upload_B=findViewById(R.id.upload_B);
        delete_F=findViewById(R.id.delete_F);
        delete_B=findViewById(R.id.delete_B);
        image_F=findViewById(R.id.f_image);
        image_B=findViewById(R.id.B_image);
        save=findViewById(R.id.save);
        bck=findViewById(R.id.bck);
        idType=findViewById(R.id.idType);
        licenceNumber=findViewById(R.id.driverLicence);
        c1=findViewById(R.id.camera1);
        c2=findViewById(R.id.camera2);
        upload_F.setOnClickListener(this);
        upload_B.setOnClickListener(this);
        delete_B.setOnClickListener(this);
        delete_F.setOnClickListener(this);
        image_F.setOnClickListener(this);
        image_B.setOnClickListener(this);
        cardView1.setOnClickListener(this);
        cardView2.setOnClickListener(this);
        save.setOnClickListener(this);
        bck.setOnClickListener(this);
        idList.add("Aadhar Card");
        idList.add("Pan Card");
        idList.add("Driving Licence");
        idType.setOptions(idList,idType);
        m = MySharedPrefrence.instanceOf(Driver_Personal_Activty.this);
//        idType.setCompoundDrawablePadding(140);




//        idType.setItem(idList);
//        idType.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
//            @Override
//            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
//                Utility.log("Selected ITem",""+parent.getSelectedItem());
//
//            }
//
//            @Override
//            public void onNothingSelected(AdapterView<?> parent) {
//
//            }
//        });
    }

    @Override
    public void onClick(View v) {
        switch (v.getId())
        {
            case R.id.upload_F:
                Pix.start(Driver_Personal_Activty.this, Options.init().setRequestCode(100).setCount(1));
                break;
            case R.id.card_1:
                Pix.start(Driver_Personal_Activty.this, Options.init().setRequestCode(100).setCount(1));
                break;
            case R.id.delete_F:
                image_F.setVisibility(View.GONE);
                c1.setVisibility(View.VISIBLE);
                frontArray.clear();
                break;
            case R.id.upload_B:
                Pix.start(Driver_Personal_Activty.this, Options.init().setRequestCode(101).setCount(1));
                break;
            case R.id.card_2:
                Pix.start(Driver_Personal_Activty.this, Options.init().setRequestCode(101).setCount(1));
                break;
            case R.id.delete_B:
                image_B.setVisibility(View.GONE);
                c2.setVisibility(View.VISIBLE);
                backtArray.clear();
                break;
            case R.id.save:
                if(! licenceNumber.getText().toString().isEmpty() && frontArray.size()>0 && backtArray.size()>0 && !idType.getText().toString().isEmpty()) {
                    progressDialog = new ProgressDialog(Driver_Personal_Activty.this);
                    progressDialog.setMessage("Uploading, please wait...");
                    progressDialog.show();
                    upLoadImage();
                }else {
                    Utility.topSnakBar(Driver_Personal_Activty.this,getWindow().getDecorView().getRootView(), Constant.PLEASE_FILL_ALL_FIELD);
                }
                break;
            case R.id.bck:
                onBackPressed();
        }

    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == Activity.RESULT_OK && requestCode == 100) {
            if(data!=null)
                frontArray = data.getStringArrayListExtra(Pix.IMAGE_RESULTS);
            if(frontArray.size()>0 && frontArray !=null){
                Glide.with(Driver_Personal_Activty.this).load(frontArray.get(0)).into(image_F);
                image_F.setVisibility(View.VISIBLE);
                c1.setVisibility(View.GONE);
            }
        }else {
            if(data!=null){
                backtArray = data.getStringArrayListExtra(Pix.IMAGE_RESULTS);
                if(backtArray.size()>0 && backtArray !=null){
                    Glide.with(Driver_Personal_Activty.this).load(backtArray.get(0)).into(image_B);
                    image_B.setVisibility(View.VISIBLE);
                    c2.setVisibility(View.GONE);
                }
            }}
    }




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
                        Utility.topSnakBar(Driver_Personal_Activty.this,getWindow().getDecorView().getRootView(),Utility.getValueFromJsonObject(jsonObject,"message"));
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                    progressDialog.dismiss();
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Utility.log("ERROR",""+error.getMessage());
            }
        });
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("key",Integer.parseInt(key));
            jsonObject.put("PIDNo", licenceNumber.getText().toString());
            jsonObject.put("name", m.getname());
            jsonObject.put("PIDType",idType.getTag());
            jsonObject.put("mobileNo", m.getMobile());
            jsonObject.put("driverTypeId",2);
            Utility.log("JSON",""+jsonObject);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        simpleMultiPartRequest.addStringParam("data",""+jsonObject.toString());
        if(frontArray!=null && frontArray.size()>0)
            simpleMultiPartRequest.addFile("PIDFrontImage",""+new File(frontArray.get(0)));
        if(frontArray!=null && frontArray.size()>0)
            simpleMultiPartRequest.addFile("PIDBackImage",""+new File(backtArray.get(0)));

        try {
            Utility.log("FinalData",""+simpleMultiPartRequest.getBody());
        } catch (AuthFailureError authFailureError) {
            authFailureError.printStackTrace();
        }
        RequestQueue requestQueue= Volley.newRequestQueue(Driver_Personal_Activty.this);
        requestQueue.add(simpleMultiPartRequest);
    }

    private void showPopup()
    {
        Rect displayRectangle = new Rect();
        Window window = Driver_Personal_Activty.this.getWindow();
        window.getDecorView().getWindowVisibleDisplayFrame(displayRectangle);
        final MaterialAlertDialogBuilder alertDialogBuilder=new MaterialAlertDialogBuilder(Driver_Personal_Activty.this,R.style.custom_dialog);
        final AlertDialog alertDialog = alertDialogBuilder.create();
        alertDialogBuilder.setMessage(getResources().getString(R.string.verifiedText));
        final View dialogView = LayoutInflater.from(Driver_Personal_Activty.this).inflate(R.layout.custom_dialog, null, false);
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
                startActivity(new Intent(Driver_Personal_Activty.this,ResponderMapsActivity.class));
                finish();
            }
        });
    }
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(Driver_Personal_Activty.this);
    }
}
