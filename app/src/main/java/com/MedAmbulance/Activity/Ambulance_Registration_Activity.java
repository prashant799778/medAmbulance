package com.MedAmbulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.app.TimePickerDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.LinearLayout;
import android.widget.TimePicker;

import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Fragments.Login_Fragment;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Regular;
import com.MedAmbulance.Widget.Atami_regular_EditText;
import com.shagi.materialdatepicker.date.DatePickerFragmentDialog;

import java.util.Calendar;

public class Ambulance_Registration_Activity extends AppCompatActivity implements View.OnClickListener {


    Atami_Regular manufactureDateText,registrationDateText;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ambulance__registration_);
        manufactureDateText=findViewById(R.id.m_date);
        registrationDateText=findViewById(R.id.r_date);
        manufactureDateText.setOnClickListener(this);
        registrationDateText.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId())
        {
            case R.id.m_date:
                Utility.log("Date","Date");
                setDate(manufactureDateText);
                break;
            case R.id.r_date:
                setDate(registrationDateText);
                break;
        }
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
        datePickerFragmentDialog.setCancelColor(Color.WHITE);
        datePickerFragmentDialog.setOkColor(Color.WHITE);
        datePickerFragmentDialog.setAccentColor(getResources().getColor(R.color.colorAccent));
        datePickerFragmentDialog.setOkText(getResources().getString(R.string.ok));
        datePickerFragmentDialog.setCancelText(getResources().getString(R.string.cancel));

    }
}
