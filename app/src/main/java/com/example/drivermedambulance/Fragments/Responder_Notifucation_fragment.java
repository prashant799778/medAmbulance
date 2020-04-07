package com.example.drivermedambulance.Fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

import com.example.drivermedambulance.R;

public class Responder_Notifucation_fragment extends Fragment {

    public Responder_Notifucation_fragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.notification_fragment, container, false);

        return rootView;
    }
}
