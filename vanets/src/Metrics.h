//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

#ifndef METRICS_H_
#define METRICS_H_

#include <omnetpp.h>
using namespace omnetpp;

/**
 * A module that just deletes every packet it receives, and collects
 * basic statistics (packet count, bit count, packet rate, bit rate).
 */
class  Metrics : public cSimpleModule
{
public:
    virtual ~Metrics(){}
    double throughputMetric;

  protected:
    simtime_t currentSimulationTime;
    double packetsDeliveredToMetrics;

    simsignal_t throughputSignal;

  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
    virtual void finish();
    virtual double updateNumberOfPacketsReceived(double packetsDeliveredToMetrics);
    virtual simtime_t getCurrentTime();
  public:
    virtual double computeThroughput(double packetsDeliveredToMetrics, double currentSimulationTime);
    double getThroughputMetric();
    double getThroughputSignal();
};


#endif /* METRICS_H_ */
