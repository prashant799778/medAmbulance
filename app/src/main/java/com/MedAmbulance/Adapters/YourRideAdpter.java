package com.MedAmbulance.Adapters;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Activity.UserRideDetailsActivity;
import com.MedAmbulance.Model.YourRidesModel;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;

import java.util.ArrayList;

public class YourRideAdpter  extends RecyclerView.Adapter <YourRideAdpter.ViewHolder>{
    private Context Ycontext;
    private ArrayList<YourRidesModel> YarrayList;

//    public YourRideAdpter(Context context, ArrayList<YourRidesModel> yourRidesModels) {
//        Ycontext=context;
//        YarrayList = yourRidesModels;
//    }

    public YourRideAdpter(Context context, ArrayList<YourRidesModel> yourRidesModels) {
        Ycontext=context;
        YarrayList = yourRidesModels;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(Ycontext).inflate(R.layout.my_ride_layout,parent,false);
        return new YourRideAdpter.ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {

        final YourRidesModel currentItem= YarrayList.get(position);
        if(currentItem.getStartTime()!=null)
            holder.date.setText(currentItem.getStartTime());
        if(currentItem.getFinalAmount()!=null)
            holder.rate.setText(currentItem.getFinalAmount());
        if(currentItem.getTripFrom()!=null)
            holder.start_Address.setText(currentItem.getTripFrom());
        if(currentItem.getTripTo()!=null)
            holder.end_Address.setText(currentItem.getTripTo());
        holder.ambu_type.setText(currentItem.getAmbulanceTypeId());
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(Ycontext, UserRideDetailsActivity.class);
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                intent.putExtra("data",currentItem);
                Ycontext.startActivity(intent);
            }
        });



    }

    @Override
    public int getItemCount() {
        return YarrayList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        Atami_Regular rate,date,start_Address,end_Address,ambu_type;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            rate=itemView.findViewById(R.id.rate);
            date=itemView.findViewById(R.id.date);
            start_Address=itemView.findViewById(R.id.start_address);
            ambu_type=itemView.findViewById(R.id.ambu_type);
            end_Address=itemView.findViewById(R.id.hospital_address);
        }
    }
}
