package com.MedAmbulance.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import com.MedAmbulance.R;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;

public class TermsConditions extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_terms_conditions);
        Animatoo.animateFade(TermsConditions.this);

    }
}
