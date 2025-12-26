"use client";

import { ResponsiveContainer, ComposedChart, Line, Area, XAxis, YAxis, Tooltip, CartesianGrid, Legend } from 'recharts';

interface DataPoint {
    date: string;
    close: number;
    predicted?: number;
}

interface StockChartProps {
    data: DataPoint[];
    predictionData?: { date: string; value: number }[];
}

const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
        return (
            <div className="bg-black/90 border border-cyan-500/30 rounded-lg p-3 backdrop-blur-sm">
                <p className="text-cyan-400 font-semibold text-xs mb-2">
                    {new Date(label).toLocaleDateString(undefined, {
                        month: 'short',
                        day: 'numeric',
                        year: 'numeric'
                    })}
                </p>
                {payload.map((entry: any, index: number) => (
                    entry.value !== null && (
                        <p key={index} className="text-xs" style={{ color: entry.color }}>
                            <strong>{entry.name}:</strong> ₹{entry.value.toFixed(2)}
                        </p>
                    )
                ))}
            </div>
        );
    }
    return null;
};

const CustomLegend = () => (
    <div className="flex justify-center gap-6 mt-4 text-sm">
        <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full bg-emerald-500"></div>
            <span className="text-gray-300">Actual Price</span>
        </div>
        <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full bg-green-500"></div>
            <span className="text-gray-300">Predicted Price</span>
        </div>
    </div>
);

export function StockChart({ data, predictionData }: StockChartProps) {
    // Prepare chart data with predictions merged
    const chartData = data.map(d => ({
        date: d.date,
        actual: d.close,
        predicted: null as number | null
    }));

    // If we have predictions, extend the data with forecast points
    if (predictionData && predictionData.length > 0) {
        // Get last actual date for connection point
        const lastActual = chartData[chartData.length - 1];

        predictionData.forEach((pred, index) => {
            chartData.push({
                date: pred.date,
                actual: index === 0 ? lastActual.actual : null, // Connect to last actual point
                predicted: pred.value
            });
        });
    }

    return (
        <div className="w-full h-[500px] mt-4">
            <ResponsiveContainer width="100%" height="100%">
                <ComposedChart data={chartData}>
                    <defs>
                        {/* Gradient for actual price area */}
                        <linearGradient id="colorActual" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="#10b981" stopOpacity={0.8} />
                            <stop offset="95%" stopColor="#10b981" stopOpacity={0.05} />
                        </linearGradient>
                        {/* Gradient for predicted area */}
                        <linearGradient id="colorPredicted" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="#22c55e" stopOpacity={0.3} />
                            <stop offset="95%" stopColor="#22c55e" stopOpacity={0.05} />
                        </linearGradient>
                    </defs>

                    <CartesianGrid
                        strokeDasharray="3 3"
                        stroke="rgba(255,255,255,0.05)"
                        vertical={false}
                    />

                    <XAxis
                        dataKey="date"
                        stroke="#64748b"
                        tick={{ fill: '#94a3b8', fontSize: 11 }}
                        tickLine={false}
                        axisLine={{ stroke: 'rgba(255,255,255,0.1)' }}
                        tickFormatter={(str) => {
                            const d = new Date(str);
                            return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
                        }}
                        angle={-15}
                        textAnchor="end"
                        height={60}
                    />

                    <YAxis
                        stroke="#64748b"
                        tick={{ fill: '#94a3b8', fontSize: 12 }}
                        tickLine={false}
                        axisLine={{ stroke: 'rgba(255,255,255,0.1)' }}
                        domain={['auto', 'auto']}
                        tickFormatter={(value) => `₹${value.toFixed(0)}`}
                    />

                    <Tooltip content={<CustomTooltip />} />

                    {/* Actual price - area with red gradient */}
                    <Area
                        type="monotone"
                        dataKey="actual"
                        stroke="#10b981"
                        strokeWidth={2}
                        fill="url(#colorActual)"
                        fillOpacity={1}
                        dot={false}
                        name="Actual"
                        connectNulls={false}
                    />

                    {/* Predicted price - line with green color */}
                    {predictionData && predictionData.length > 0 && (
                        <>
                            <Area
                                type="monotone"
                                dataKey="predicted"
                                stroke="#22c55e"
                                strokeWidth={2.5}
                                strokeDasharray="5 5"
                                fill="url(#colorPredicted)"
                                fillOpacity={1}
                                dot={{ fill: '#22c55e', r: 4 }}
                                name="Predicted"
                                connectNulls={true}
                            />
                        </>
                    )}
                </ComposedChart>
            </ResponsiveContainer>
            <CustomLegend />
        </div>
    );
}
