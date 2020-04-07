package com.example.respondermedambulance.Fragments;


import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

import com.example.respondermedambulance.R;

public class RateCardFragment extends Fragment {

    public RateCardFragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.frag_ratecard, container, false);

        return rootView;
    }
}
