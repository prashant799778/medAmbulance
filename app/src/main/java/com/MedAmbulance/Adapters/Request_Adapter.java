package com.MedAmbulance.Adapters;

import android.content.Context;
import android.os.Build;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.recyclerview.widget.RecyclerView;

import com.MedAmbulance.Model.Request;
import com.MedAmbulance.R;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;


public class Request_Adapter extends RecyclerView.Adapter<Request_Adapter.MyViewHolder> {

        private List<Request> requestsList;
        Context context;

        public class MyViewHolder extends RecyclerView.ViewHolder {
            public TextView title, year, genre;

            public MyViewHolder(View view) {
                super(view);
                //title = (TextView) view.findViewById(R.id.title);

            }
        }


        public Request_Adapter(List<Request> requests,Context context) {

            this.requestsList =requests;
            this.context=context;
        }

        @Override
        public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
            View itemView = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.driver_request_view, parent, false);

            return new MyViewHolder(itemView);
        }

        @Override
        public void onBindViewHolder(MyViewHolder holder, int position) {
           Request movie = requestsList.get(position);

        }

        @Override
        public int getItemCount() {
            return  requestsList.size();
        }
    }