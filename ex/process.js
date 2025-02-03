// processor.js
class DataProcessor {
    static processKey(input) {
        return Buffer.from(input, 'hex').toString('base64');
    }
    
    static getVenueDetails() {
        return {
            'location': 'Downtown Music District',
            'parking': 2000,
            'stages': ['Main Stage', 'Electronic Stage', 'Acoustic Stage'],
            'key': '4354467B417374687261' // Part of verification
        };
    }
}