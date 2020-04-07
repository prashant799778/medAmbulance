package com.example.respondermedambulance.Fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

import com.example.respondermedambulance.R;

public class Notifucation_fragment extends Fragment {

    public Notifucation_fragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.notification_fragment, container, false);

        return rootView;
    }
}
