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

package vanets;

import org.car2x.veins.modules.mac.ieee80211p.Mac1609_4; 

simple Mac16094Metrics extends Mac1609_4
{
    parameters:
        @signal[throughputSignalMac](type=double);
        @statistic[throughputMetricMac](title="throughputMetricMac"; source="throughputSignalMac"; record=last,count,sum, mean, vector?);
        //@statistic[throughputMbps](title="throughputMbps"; source 
	    @class(Mac16094Metrics); 
}