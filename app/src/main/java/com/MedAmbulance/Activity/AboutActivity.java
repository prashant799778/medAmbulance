package com.MedAmbulance.Activity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import com.MedAmbulance.R;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;

public class AboutActivity extends AppCompatActivity {

    ImageView move_back;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);
        Animatoo.animateSwipeLeft(AboutActivity.this);

        move_back = findViewById(R.id.move_back);
        move_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSwipeLeft(AboutActivity.this);
    }
}
