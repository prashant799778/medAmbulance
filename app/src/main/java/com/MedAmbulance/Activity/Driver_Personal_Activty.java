package com.MedAmbulance.Activity;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ImageView;

import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_regular_EditText;
import com.MedAmbulance.Widget.Custom_Spinner;
import com.bumptech.glide.Glide;
import com.fxn.pix.Options;
import com.fxn.pix.Pix;
import com.google.android.material.card.MaterialCardView;


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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver__personal__activty);
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
        idList.add("Pen Card");
        idList.add("Driving Licence");
//        idType.setOptions(idList);
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
                if(frontArray.size()>0 && backtArray.size()>0)
                    onBackPressed();
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

}
