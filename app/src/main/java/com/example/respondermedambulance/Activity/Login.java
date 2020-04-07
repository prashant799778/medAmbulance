package com.example.respondermedambulance.Activity;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.example.respondermedambulance.Adapters.Login_SignUp_Adapter;
import com.example.respondermedambulance.Comman.Utility;
import com.example.respondermedambulance.Comman.Validation;
import com.example.respondermedambulance.R;
import com.example.respondermedambulance.Widget.Atami_Bold;
import com.example.respondermedambulance.Widget.Atami_regular_EditText;
import com.andrognito.flashbar.Flashbar;
import com.andrognito.flashbar.anim.FlashAnim;
import com.blogspot.atifsoftwares.animatoolib.Animatoo;
import com.google.android.material.tabs.TabLayout;

public class Login extends AppCompatActivity  {
    Login_SignUp_Adapter adapter;
    TabLayout tabLayout;
    ViewPager viewPager;
    String userType="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        Animatoo.animateSlideLeft(Login.this);
        Intent i = getIntent();
        if (i != null)
            userType = i.getStringExtra("userType");
        adapter = new Login_SignUp_Adapter(
                getSupportFragmentManager(), Login.this, userType);
        viewPager = (ViewPager) findViewById(R.id.viewpager);
        viewPager.setAdapter(adapter);
        tabLayout = (TabLayout) findViewById(R.id.tabs);
        tabLayout.setupWithViewPager(viewPager);
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Animatoo.animateSlideRight(Login.this);
    }
}