"use client";

import { useState, useRef, useEffect } from 'react';
import { Search } from 'lucide-react';

interface SearchResult {
    symbol: string;
    name: string;
    exchange: string;
    match_type: string;
}

interface SearchDropdownProps {
    value: string;
    onSelect: (symbol: string) => void;
    placeholder?: string;
}

export function SearchDropdown({ value, onSelect, placeholder = "Search Ticker..." }: SearchDropdownProps) {
    const [query, setQuery] = useState(value);
    const [results, setResults] = useState<SearchResult[]>([]);
    const [isOpen, setIsOpen] = useState(false);
    const [selectedIndex, setSelectedIndex] = useState(-1);
    const dropdownRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        setQuery(value);
    }, [value]);

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                setIsOpen(false);
            }
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    const handleSearch = async (searchQuery: string) => {
        setQuery(searchQuery);

        if (searchQuery.length < 1) {
            setResults([]);
            setIsOpen(false);
            return;
        }

        try {
            const res = await fetch(`http://localhost:8000/api/v1/search?q=${encodeURIComponent(searchQuery)}&limit=10`);
            if (res.ok) {
                const data = await res.json();
                setResults(data);
                setIsOpen(data.length > 0);
                setSelectedIndex(-1);
            }
        } catch (e) {
            console.error('Search error:', e);
        }
    };

    const handleSelect = (symbol: string) => {
        setQuery(symbol);
        onSelect(symbol);
        setIsOpen(false);
        setResults([]);
    };

    const handleKeyDown = (e: React.KeyboardEvent) => {
        if (!isOpen) return;

        switch (e.key) {
            case 'ArrowDown':
                e.preventDefault();
                setSelectedIndex(prev => (prev < results.length - 1 ? prev + 1 : prev));
                break;
            case 'ArrowUp':
                e.preventDefault();
                setSelectedIndex(prev => (prev > 0 ? prev - 1 : -1));
                break;
            case 'Enter':
                e.preventDefault();
                if (selectedIndex >= 0 && selectedIndex < results.length) {
                    handleSelect(results[selectedIndex].symbol);
                }
                break;
            case 'Escape':
                setIsOpen(false);
                break;
        }
    };

    const highlightMatch = (text: string, query: string) => {
        const index = text.toUpperCase().indexOf(query.toUpperCase());
        if (index === -1) return text;

        return (
            <>
                {text.substring(0, index)}
                <span className="text-blue-400 font-semibold">
                    {text.substring(index, index + query.length)}
                </span>
                {text.substring(index + query.length)}
            </>
        );
    };

    return (
        <div className="relative group" ref={dropdownRef}>
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 group-focus-within:text-blue-400 transition-colors" />
            <input
                value={query}
                onChange={(e) => handleSearch(e.target.value)}
                onKeyDown={handleKeyDown}
                onFocus={() => {
                    if (results.length > 0) setIsOpen(true);
                }}
                className="bg-white/5 border border-white/10 rounded-full py-2 pl-10 pr-4 text-sm focus:outline-none focus:border-blue-500/50 w-64 transition-all"
                placeholder={placeholder}
            />

            {isOpen && results.length > 0 && (
                <div className="absolute top-full mt-2 w-full bg-gray-900/95 backdrop-blur-xl border border-white/10 rounded-lg shadow-2xl overflow-hidden z-50">
                    {results.map((result, index) => (
                        <div
                            key={result.symbol}
                            onClick={() => handleSelect(result.symbol)}
                            className={`px-4 py-3 cursor-pointer transition-colors border-b border-white/5 last:border-b-0 ${index === selectedIndex
                                    ? 'bg-blue-500/20'
                                    : 'hover:bg-white/5'
                                }`}
                        >
                            <div className="flex justify-between items-center">
                                <div>
                                    <div className="font-medium text-white">
                                        {highlightMatch(result.symbol, query)}
                                    </div>
                                    <div className="text-xs text-gray-400 mt-0.5">
                                        {highlightMatch(result.name, query)}
                                    </div>
                                </div>
                                <div className="text-xs text-gray-500 bg-white/5 px-2 py-1 rounded">
                                    {result.exchange}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}
