"use client";

import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

interface DataPoint {
    date: string;
    close: number;
}

interface StockChartProps {
    data: DataPoint[];
    predictionData?: DataPoint[];
}

export function StockChart({ data, predictionData }: StockChartProps) {
    // Combine data or just show main data for now.
    // We can overlay predictions if timestamps align, or append them.

    // For simplicity, let's just render the passed data. 
    // If predictionData exists, we might want to append it with a different key for coloring.

    const formattedData = data.map(d => ({
        ...d,
        date: new Date(d.date).toLocaleDateString(),
        value: d.close
    }));

    // Append predictions if any
    const combinedData = [...formattedData];
    if (predictionData && predictionData.length > 0) {
        // Connect last real point to first pred point
        // predictionData logic to be handled by parent or here
        predictionData.forEach(d => {
            combinedData.append({
                date: new Date(d.date).toLocaleDateString(),
                predicted: d.close
            } as any)
        })
    }

    return (
        <div className="w-full h-[400px] mt-4">
            <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={data}>
                    <defs>
                        <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="#00f2fe" stopOpacity={0.3} />
                            <stop offset="95%" stopColor="#00f2fe" stopOpacity={0} />
                        </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                    <XAxis
                        dataKey="date"
                        stroke="#64748b"
                        tick={{ fill: '#64748b', fontSize: 12 }}
                        tickLine={false}
                        axisLine={false}
                        tickFormatter={(str) => str ? new Date(str).toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) : ''}
                    />
                    <YAxis
                        stroke="#64748b"
                        tick={{ fill: '#64748b', fontSize: 12 }}
                        tickLine={false}
                        axisLine={false}
                        domain={['auto', 'auto']}
                    />
                    <Tooltip
                        contentStyle={{ backgroundColor: 'rgba(0,0,0,0.8)', border: 'none', borderRadius: '8px' }}
                        itemStyle={{ color: '#fff' }}
                    />
                    <Area
                        type="monotone"
                        dataKey="close"
                        stroke="#00f2fe"
                        strokeWidth={2}
                        fillOpacity={1}
                        fill="url(#colorValue)"
                    />
                </AreaChart>
            </ResponsiveContainer>
        </div>
    );
}
