package com.MedAmbulance.Adapters;

import android.content.Context;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Fragments.Login_Fragment;
import com.MedAmbulance.Fragments.SignUp_Fragment;
import com.MedAmbulance.R;
public   class Login_SignUp_Adapter extends FragmentPagerAdapter {
    private static int NUM_ITEMS = 2;
    private static  String title[]= null;
    String userType="3";

    MySharedPrefrence m;
    public Login_SignUp_Adapter(FragmentManager fragmentManager, Context context,String userType) {
        super(fragmentManager);
        this.userType=userType;
       title= new String[]{context.getResources().getString(R.string.Login),context.getResources().getString(R.string.signup)};
    }

    // Returns total number of pages
    @Override
    public int getCount() {
        return NUM_ITEMS;
    }

    // Returns the fragment to display for that page
    @Override
    public Fragment getItem(int position) {
        switch (position) {
            case 0: // Fragment # 0 - This will show FirstFragment
                return new Login_Fragment(userType);
            case 1: // Fragment # 0 - This will show FirstFragment
                return new SignUp_Fragment(userType);
            default:
                return null;
        }
    }
    // Returns the page title for the top indicator
    @Override
    public CharSequence getPageTitle(int position) {
        return title[position];
    }


    @Override
    public int getItemPosition(@NonNull Object object) {
        return POSITION_NONE;
    }
}

