package com.example.drivermedambulance.Activity;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.app.ProgressDialog;
import android.app.TimePickerDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Rect;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TimePicker;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.error.AuthFailureError;
import com.android.volley.error.VolleyError;
import com.android.volley.request.SimpleMultiPartRequest;
import com.android.volley.toolbox.Volley;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.bumptech.glide.Glide;
import com.example.drivermedambulance.Comman.Constant;
import com.example.drivermedambulance.Comman.MySharedPrefrence;
import com.example.drivermedambulance.Comman.URLS;
import com.example.drivermedambulance.Comman.Utility;
import com.example.drivermedambulance.Fragments.Login_Fragment;
import com.example.drivermedambulance.Model.Ambulance;
import com.example.drivermedambulance.R;
import com.example.drivermedambulance.Widget.Atami_Bold;
import com.example.drivermedambulance.Widget.Atami_Regular;
import com.example.drivermedambulance.Widget.Atami_regular_EditText;
import com.example.drivermedambulance.Widget.Custom_Spinner;
import com.example.drivermedambulance.Widget.Custom_Spinner_For_TextValue;
import com.fxn.pix.Options;
import com.fxn.pix.Pix;
import com.google.android.material.card.MaterialCardView;
import com.google.android.material.dialog.MaterialAlertDialogBuilder;
import com.shagi.materialdatepicker.date.DatePickerFragmentDialog;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;
import java.util.Calendar;

public class Ambulance_Registration_Activity extends AppCompatActivity {


    Atami_Regular manufactureDateText,registrationDateText;
    ArrayList<String>categoryList;
    ArrayList<String>model;
    ArrayList<String>type;
    ArrayList<String>fuel;
    String key="3";
    ArrayList<String>frontArray;
    ImageView bck;
    Button save;
    ProgressDialog progressDialog;
    Atami_regular_EditText registration;
    MySharedPrefrence m;
    MaterialCardView uploard_Image;
    ImageView delete_Image,uploard_Image1,f_image,fake_camare;
    Custom_Spinner ambulance_category,ambulanceType;
    Custom_Spinner_For_TextValue ambulance_model,fueltype;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ambulance__registration_);
        Animatoo.animateSlideLeft(Ambulance_Registration_Activity.this);
        categoryList=new ArrayList<>();
        model=new ArrayList<>();
        fuel=new ArrayList<>();
        type=new ArrayList<>();

        frontArray=new ArrayList<>();
        categoryList.add("Government");
        categoryList.add("Private");
        categoryList.add("Hospital");


        type.add("ALS");
        type.add("BLS");
        type.add("PVT");


        model.add("2001");
        model.add("2002");
        model.add("2003");

        model.add("2004");
        model.add("2005");
        model.add("2006");

        model.add("2007");
        model.add("2008");
        model.add("2009");

        fuel.add("Petrol");
        fuel.add("Diesel");
        fuel.add("CNG");


        m= MySharedPrefrence.instanceOf(Ambulance_Registration_Activity.this);
        f_image=findViewById(R.id.f_image);
        bck=findViewById(R.id.bck);
        fake_camare=findViewById(R.id.camera1);
        manufactureDateText=findViewById(R.id.m_date);
        registrationDateText=findViewById(R.id.r_date);
        ambulance_category=findViewById(R.id.idType);
        uploard_Image=findViewById(R.id.card_1);
        delete_Image=findViewById(R.id.delete_F);
        uploard_Image1=findViewById(R.id.upload_F);
        ambulanceType=findViewById(R.id.idType1);
        save=findViewById(R.id.save);
        ambulance_model=findViewById(R.id.idType2);
        registration=findViewById(R.id.idType4);
        fueltype=findViewById(R.id.idType5);
        ambulance_category.setOptions(categoryList,ambulance_category);
        ambulanceType.setOptions(type,ambulanceType);
        ambulance_model.setOptions(model,ambulance_model);
        fueltype.setOptions(fuel,fueltype);
        manufactureDateText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setDate(manufactureDateText);
            }
        });
        registrationDateText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                 setDate(registrationDateText); }
        });


        bck.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });


        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!ambulance_category.getText().toString().isEmpty() && !ambulanceType.getText().toString().isEmpty() && !ambulance_model.getText().toString().isEmpty()
                 && !registration.getText().toString().isEmpty() && !fueltype.getText().toString().isEmpty() && !manufactureDateText.getText().toString().isEmpty() && !registrationDateText.getText().toString().isEmpty()){
                    progressDialog = new ProgressDialog(Ambulance_Registration_Activity.this);
                    progressDialog.setMessage("Uploading, please wait...");
                    progressDialog.show();
                    upLoadImage();}else {
                    Utility.topSnakBar(Ambulance_Registration_Activity.this,getWindow().getDecorView().getRootView(), Constant.PLEASE_FILL_ALL_FIELD);
                }
            }
        });
        uploard_Image.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Pix.start(Ambulance_Registration_Activity.this, Options.init().setRequestCode(100).setCount(1));
            }
        });
        uploard_Image1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Pix.start(Ambulance_Registration_Activity.this, Options.init().setRequestCode(100).setCount(1));
            }
        });
        delete_Image.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                f_image.setVisibility(View.GONE);
                fake_camare.setVisibility(View.VISIBLE);
                frontArray.clear();
            }
        });
    }
    public void setDate(final Atami_Regular textview)
    {
        final Calendar cldr = Calendar.getInstance();
        int day = cldr.get(Calendar.DAY_OF_MONTH);
        int month = cldr.get(Calendar.MONTH);
        int year = cldr.get(Calendar.YEAR);
        DatePickerFragmentDialog datePickerFragmentDialog=DatePickerFragmentDialog.newInstance(new DatePickerFragmentDialog.OnDateSetListener() {
            @Override
            public void onDateSet(DatePickerFragmentDialog view, int year, int monthOfYear, int dayOfMonth) {
                textview.setText(dayOfMonth + "/" + (monthOfYear + 1) + "/" + year);
            }
        },year, month, day);
        datePickerFragmentDialog.show(getSupportFragmentManager(),null);
        datePickerFragmentDialog.setMaxDate(System.currentTimeMillis());
        datePickerFragmentDialog.setYearRange(1900,year);
        datePickerFragmentDialog.setCancelColor(Color.BLACK);
        datePickerFragmentDialog.setOkColor(Color.BLACK);
        datePickerFragmentDialog.setOkText("Ok");
        datePickerFragmentDialog.setCancelText(getResources().getString(R.string.cancel));

    }
    private void upLoadImage()
    {
        SimpleMultiPartRequest simpleMultiPartRequest=new SimpleMultiPartRequest(Request.Method.POST, URLS.AddLicence, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                Utility.log("Response",""+response);
                try {
                    JSONObject jsonObject=new JSONObject(response);
                    if(Boolean.parseBoolean(jsonObject.getString("status")))
                    {
                        progressDialog.dismiss();
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
                        Utility.topSnakBar(Ambulance_Registration_Activity.this,getWindow().getDecorView().getRootView(),Utility.getValueFromJsonObject(jsonObject,"message"));
                    }
                } catch (JSONException e) {
                    progressDialog.dismiss();
                    e.printStackTrace();
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Utility.log("ERROR",""+error.getMessage());
                progressDialog.dismiss();
            }
        });
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("key",Integer.parseInt(key));
            jsonObject.put("name", m.getname());
            jsonObject.put("mobileNo", m.getMobile());
            jsonObject.put("driverTypeId",1);
            jsonObject.put("lat",77.33);
            jsonObject.put("lng",77.33);
            jsonObject.put("TransportType",""+ambulance_model.getTag());
            jsonObject.put("AmbulanceTypeId",""+ambulanceType.getTag());
            jsonObject.put("AmbulanceRegistrationFuel",""+fueltype.getTag());
            jsonObject.put("AmbulanceModeId",""+ambulance_model.getTag());
            jsonObject.put("AmbulanceNo",""+registration.getText().toString());
            jsonObject.put("manufactureDate",""+manufactureDateText.getText().toString());
            jsonObject.put("RegistrationDate",""+registrationDateText.getText().toString());
            Utility.log("JSON",""+jsonObject);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        simpleMultiPartRequest.addStringParam("data",""+jsonObject.toString());
        if(frontArray!=null && frontArray.size()>0)
            simpleMultiPartRequest.addFile("AmbulanceImage",""+new File(frontArray.get(0)));

        try {
            Utility.log("FinalData",""+simpleMultiPartRequest.getBody());
        } catch (AuthFailureError authFailureError) {
            authFailureError.printStackTrace();
        }
        RequestQueue requestQueue= Volley.newRequestQueue(Ambulance_Registration_Activity.this);
        requestQueue.add(simpleMultiPartRequest);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == Activity.RESULT_OK && requestCode == 100) {
            if(data!=null)
                frontArray = data.getStringArrayListExtra(Pix.IMAGE_RESULTS);
            if(frontArray.size()>0 && frontArray !=null){
                Glide.with(Ambulance_Registration_Activity.this).load(frontArray.get(0)).into(f_image);
                f_image.setVisibility(View.VISIBLE);
                fake_camare.setVisibility(View.GONE);
            }
        }
    }


    private void showPopup()
    {
        Rect displayRectangle = new Rect();
        Window window = Ambulance_Registration_Activity.this.getWindow();
        window.getDecorView().getWindowVisibleDisplayFrame(displayRectangle);
        final MaterialAlertDialogBuilder alertDialogBuilder=new MaterialAlertDialogBuilder(Ambulance_Registration_Activity.this,R.style.custom_dialog);
        final AlertDialog alertDialog = alertDialogBuilder.create();
        alertDialogBuilder.setMessage(getResources().getString(R.string.verifiedText));
        final View dialogView = LayoutInflater.from(Ambulance_Registration_Activity.this).inflate(R.layout.custom_dialog, null, false);
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
                startActivity(new Intent(Ambulance_Registration_Activity.this,DriversMapsActivity.class));
                finish();
            }
        });
    }
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(Ambulance_Registration_Activity.this);
    }
}
