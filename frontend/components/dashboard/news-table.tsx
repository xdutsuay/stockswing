import { motion, AnimatePresence } from 'framer-motion';
import { ExternalLink, TrendingUp, TrendingDown, Minus, ChevronDown, ChevronUp, Loader2 } from 'lucide-react';
import { useState } from 'react';

interface NewsArticle {
    ticker: string;
    title: string;
    url: string;
    published_date: string;
    source: string;
    summary: string;
    sentiment_score: number;
    sentiment_label: string;
    impact_score: number;
    evidence: string;
}

interface NewsTableProps {
    news: NewsArticle[];
    isLoading?: boolean;
}

export function NewsTable({ news, isLoading = false }: NewsTableProps) {
    const [expandedId, setExpandedId] = useState<number | null>(null);

    const getSentimentColor = (label: string) => {
        switch (label) {
            case 'Bullish': return 'text-green-400 border-green-400/30 bg-green-400/10';
            case 'Bearish': return 'text-red-400 border-red-400/30 bg-red-400/10';
            default: return 'text-gray-400 border-gray-400/30 bg-gray-400/10';
        }
    };

    const getSentimentIcon = (label: string) => {
        switch (label) {
            case 'Bullish': return <TrendingUp className="w-4 h-4" />;
            case 'Bearish': return <TrendingDown className="w-4 h-4" />;
            default: return <Minus className="w-4 h-4" />;
        }
    };

    const formatDate = (dateStr: string) => {
        return new Date(dateStr).toLocaleDateString(undefined, {
            month: 'short', day: 'numeric', year: 'numeric'
        });
    };

    if (isLoading) {
        return (
            <div className="w-full flex justify-center items-center py-12">
                <Loader2 className="w-8 h-8 text-blue-400 animate-spin" />
            </div>
        );
    }

    if (!news || news.length === 0) return (
        <div className="text-center py-8 text-gray-500 text-sm">No news available for this ticker.</div>
    );

    return (
        <div className="w-full overflow-hidden">
            <div className="grid grid-cols-12 gap-4 px-4 py-3 text-xs font-medium text-gray-400 uppercase tracking-wider border-b border-white/10">
                <div className="col-span-6 md:col-span-5">Article</div>
                <div className="col-span-3 md:col-span-2">Date</div>
                <div className="col-span-3 md:col-span-2">Sentiment</div>
                <div className="hidden md:block md:col-span-2">Impact</div>
                <div className="hidden md:block md:col-span-1 text-right">Action</div>
            </div>

            <div className="divide-y divide-white/5">
                {news.map((article, index) => (
                    <div key={index} className="group">
                        <div
                            className="grid grid-cols-12 gap-4 px-4 py-4 items-center hover:bg-white/5 transition-colors cursor-pointer"
                            onClick={() => setExpandedId(expandedId === index ? null : index)}
                        >
                            <div className="col-span-6 md:col-span-5 pr-4">
                                <h4 className="text-sm font-medium text-white group-hover:text-blue-400 transition-colors line-clamp-1">
                                    <a href={article.url} target="_blank" rel="noopener noreferrer" onClick={(e) => e.stopPropagation()}>
                                        {article.title}
                                    </a>
                                </h4>
                                <div className="flex items-center gap-2 mt-1 text-xs text-gray-500">
                                    <span className="px-1.5 py-0.5 rounded bg-white/10 text-gray-300">{article.source}</span>
                                </div>
                            </div>

                            <div className="col-span-3 md:col-span-2 text-sm text-gray-400">
                                {formatDate(article.published_date)}
                            </div>

                            <div className="col-span-3 md:col-span-2">
                                <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border ${getSentimentColor(article.sentiment_label)}`}>
                                    {getSentimentIcon(article.sentiment_label)}
                                    {article.sentiment_label}
                                </span>
                            </div>

                            <div className="hidden md:block md:col-span-2">
                                <div className="flex items-center gap-2">
                                    <div className="flex-1 h-1.5 bg-white/10 rounded-full overflow-hidden">
                                        <div
                                            className={`h-full rounded-full ${article.sentiment_label === 'Bullish' ? 'bg-green-500' : article.sentiment_label === 'Bearish' ? 'bg-red-500' : 'bg-gray-500'}`}
                                            style={{ width: `${article.impact_score}%` }}
                                        />
                                    </div>
                                    <span className="text-xs text-gray-400 w-6">{article.impact_score}</span>
                                </div>
                            </div>

                            <div className="hidden md:block md:col-span-1 text-right">
                                {expandedId === index ? <ChevronUp className="w-5 h-5 text-gray-500 ml-auto" /> : <ChevronDown className="w-5 h-5 text-gray-500 ml-auto" />}
                            </div>
                        </div>

                        <AnimatePresence>
                            {expandedId === index && (
                                <motion.div
                                    initial={{ height: 0, opacity: 0 }}
                                    animate={{ height: 'auto', opacity: 1 }}
                                    exit={{ height: 0, opacity: 0 }}
                                    className="overflow-hidden bg-black/20"
                                >
                                    <div className="p-4 border-t border-white/5 space-y-4">
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                            <div>
                                                <h5 className="text-xs font-semibold text-gray-400 uppercase mb-2">Summary</h5>
                                                <p className="text-sm text-gray-300 leading-relaxed">{article.summary}</p>
                                            </div>
                                            {article.evidence && (
                                                <div>
                                                    <h5 className="text-xs font-semibold text-gray-400 uppercase mb-2">AI Key Insights</h5>
                                                    <div className="text-sm text-gray-300">
                                                        {/* Parse string array if needed, for simulated data it's a string representation of list */}
                                                        {article.evidence.replace(/[\[\]']/g, '').split(',').map((item, i) => (
                                                            item.trim() && (
                                                                <div key={i} className="flex items-start gap-2 mb-1">
                                                                    <span className="text-blue-400">•</span>
                                                                    <span>{item.trim()}</span>
                                                                </div>
                                                            )
                                                        ))}
                                                    </div>
                                                </div>
                                            )}
                                        </div>
                                        <div className="flex justify-end pt-2">
                                            <a
                                                href={article.url}
                                                target="_blank"
                                                rel="noopener noreferrer"
                                                className="inline-flex items-center gap-2 text-sm text-cyan-400 hover:text-cyan-300 hover:underline"
                                            >
                                                Read full article <ExternalLink className="w-3 h-3" />
                                            </a>
                                        </div>
                                    </div>
                                </motion.div>
                            )}
                        </AnimatePresence>
                    </div>
                ))}
            </div>
        </div>
    );
}
