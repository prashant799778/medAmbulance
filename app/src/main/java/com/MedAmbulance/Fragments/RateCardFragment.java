package com.MedAmbulance.Fragments;


import android.app.ProgressDialog;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

import com.MedAmbulance.Api_Calling.MyResult;
import com.MedAmbulance.Comman.Api_Calling;
import com.MedAmbulance.Comman.URLS;
import com.MedAmbulance.Comman.Utility;
import com.MedAmbulance.Model.RateCardModel;
import com.MedAmbulance.Model.YourRidesModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;
import com.MedAmbulance.Widget.Custom_Spinner;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class RateCardFragment extends Fragment implements MyResult {

    public RateCardFragment() {
    }
    Atami_Bold title;
    ProgressDialog progressDialog;
    MyResult result;
    Custom_Spinner spinner;
    Atami_Regular category,fair_per_km,miniDis,miniFair,waitFair;
    ArrayList<String>arrayList;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.frag_ratecard, container, false);
        arrayList=new ArrayList<>();
        arrayList.add("Government");
        arrayList.add("Private");
        arrayList.add("Hospital");
        this.result=this;
        title=rootView.findViewById(R.id.title);
        spinner=rootView.findViewById(R.id.idType);
        category=rootView.findViewById(R.id.ambulanceCategory);
        fair_per_km=rootView.findViewById(R.id.prkm);
        miniDis=rootView.findViewById(R.id.minimumDistance);
        miniFair=rootView.findViewById(R.id.minimumfair);
        waitFair=rootView.findViewById(R.id.waitfair);
        progressDialog = new ProgressDialog(getContext());
        progressDialog.setMessage(" Please wait ...");
        progressDialog.setCancelable(true);
                spinner.setOptions(arrayList,spinner,this);
        return rootView;
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
         progressDialog.dismiss();
        if(object!=null && status)
        {
            Gson gson= new GsonBuilder().create();
            try {
                ArrayList<RateCardModel> rm = gson.fromJson(object.getString("result"), new TypeToken<ArrayList<RateCardModel>>(){}.getType());
                title.setText(""+spinner.getText().toString());
                category.setText(rm.get(0).getCategory());
                fair_per_km.setText(rm.get(0).getFarePerKM()+" Per/Km");
                miniFair.setText(rm.get(0).getMinFare());
                miniDis.setText(rm.get(0).getMinDistance()+" Km");
                waitFair.setText(rm.get(0).getWaitFare());
            } catch (JSONException e) {
                e.printStackTrace();
            }

        }

    }
    public  void callApi()
    {
        progressDialog.show();
        Api_Calling.postMethodCall(getContext(), URLS.getFareManagement,getActivity().getWindow().getDecorView().getRootView(),result,"",jsonObject(spinner.getTag().toString()));
    }
    public JSONObject jsonObject(String id)
    {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("categoryId",""+id);
            Utility.log("JSON",""+jsonObject);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;
    }
}
