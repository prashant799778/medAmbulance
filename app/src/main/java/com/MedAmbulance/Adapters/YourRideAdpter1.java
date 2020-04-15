package com.MedAmbulance.Adapters;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Activity.UserRideDetailsActivity;
import com.MedAmbulance.Model.YourRidesModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Regular;

import java.util.ArrayList;

public class YourRideAdpter1 extends RecyclerView.Adapter <YourRideAdpter1.ViewHolder>{
    private Context Ycontext;
    private ArrayList<YourRidesModel> YarrayList;

//    public YourRideAdpter(Context context, ArrayList<YourRidesModel> yourRidesModels) {
//        Ycontext=context;
//        YarrayList = yourRidesModels;
//    }

    public YourRideAdpter1(Context context, ArrayList<YourRidesModel> yourRidesModels) {
        Ycontext=context;
        YarrayList = yourRidesModels;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(Ycontext).inflate(R.layout.responder_trip_item_view,parent,false);
        return new YourRideAdpter1.ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {

        final YourRidesModel currentItem= YarrayList.get(position);
        if(currentItem.getStartTime()!=null)
            holder.date.setText(currentItem.getStartTime());
        if(currentItem.getTripFrom()!=null)
            holder.start_Address.setText(currentItem.getTripFrom());
        if(currentItem.getFinalAmount()!=null)
            holder.rate.setText(currentItem.getFinalAmount());
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
            ambu_type=itemView.findViewById(R.id.ambu_type);
            start_Address=itemView.findViewById(R.id.start_address);
            end_Address=itemView.findViewById(R.id.hospital_address);
        }
    }
}
