package com.MedAmbulance.Adapters;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Activity.DetailsActivity;
import com.MedAmbulance.Model.myTripModel;
import com.MedAmbulance.R;
import com.MedAmbulance.Widget.Atami_Bold;
import com.MedAmbulance.Widget.Atami_Regular;

import java.util.ArrayList;

public class ResponderTripAdapter extends RecyclerView.Adapter <ResponderTripAdapter.ViewHolder>{

    private Context mcontext;
    private ArrayList<myTripModel> marrayList;

    public ResponderTripAdapter(Context context, ArrayList<myTripModel> myTripModels) {
       mcontext=context;
       marrayList = myTripModels;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(mcontext).inflate(R.layout.responder_trip_item_view,parent,false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
     final myTripModel currentItem= marrayList.get(position);


     if (currentItem.getStartTime()!=null)
     holder.date.setText(currentItem.getStartTime());
        if (currentItem.getFinalAmount()!=null)
     holder.rate.setText(currentItem.getFinalAmount());
        if (currentItem.getTripFrom()!=null)
        holder.start_address.setText(currentItem.getTripFrom());
        if (currentItem.getTripTo()!=null)
        holder.end_address.setText(currentItem.getTripTo());
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(mcontext, DetailsActivity.class);
                intent.putExtra("data",currentItem);
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                mcontext.startActivity(intent);
            }
        });
    }

    @Override
    public int getItemCount() {
        return marrayList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{
        Atami_Regular rate,date,start_address,end_address;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            rate=itemView.findViewById(R.id.rate);
            date =itemView.findViewById(R.id.date);
            start_address=itemView.findViewById(R.id.start_address);
            end_address=itemView.findViewById(R.id.hospital_address);
        }
    }
}
