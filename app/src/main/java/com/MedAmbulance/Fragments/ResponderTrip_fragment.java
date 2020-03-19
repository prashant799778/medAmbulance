package com.MedAmbulance.Fragments;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Adapters.MyTripAdapter;
import com.MedAmbulance.Adapters.ResponderTripAdapter;
import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.MySharedPrefrence;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class ResponderTrip_fragment extends Fragment implements MyResult {

    MyResult myResult;
    MySharedPrefrence m;
    ProgressDialog progressDialog;

    private RecyclerView mrecyclerView;
    private ResponderTripAdapter myTripAdapter;
    RelativeLayout relativeLayout;
    private ArrayList<myTripModel> MarrayList;

    public ResponderTrip_fragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        m = MySharedPrefrence.instanceOf(getContext());
        this.myResult=this;
        View rootView = inflater.inflate(R.layout.my_trip_fragment, container, false);
        relativeLayout=rootView.findViewById(R.id.no_data);
        progressDialog = new ProgressDialog(getContext());
        progressDialog.setMessage(" Please wait ...");
        progressDialog.setCancelable(true);
        progressDialog.show();
        mrecyclerView=rootView.findViewById(R.id.my_trips);

        mrecyclerView.setHasFixedSize(true);
        mrecyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        MarrayList= new ArrayList<>();
        myTripAdapter=new ResponderTripAdapter(getContext(),MarrayList);
        mrecyclerView.setAdapter(myTripAdapter);
        Api_Calling.postMethodCall(getContext(), URLS.MyTrips,getActivity().getWindow().getDecorView().getRootView(),myResult,"Mytrip",MyTripObject());

        return rootView;
    }

    private JSONObject MyTripObject() {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("userId",""+m.getUserId());
            Log.d("Mytrip", "profileObject: "+jsonObject);

        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }
    @Override
    public void onResult(JSONObject object, Boolean status) {

        Log.d("AG", "onResult: "+object);
        if (progressDialog!=null &&  progressDialog.isShowing())
            progressDialog.dismiss();
        if(object!=null && status){
            relativeLayout.setVisibility(View.GONE);

            Gson gson= new GsonBuilder().create();
            try {
                ArrayList<myTripModel> rm = gson.fromJson(object.getString("result"), new TypeToken<ArrayList<myTripModel>>(){}.getType());
                MarrayList.clear();
                MarrayList.addAll(rm);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            myTripAdapter.notifyDataSetChanged();
        }

    }
}
